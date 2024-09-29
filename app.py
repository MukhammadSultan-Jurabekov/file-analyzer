import ast
import os

class PythonAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = []
        self.functions = []
        self.classes = []
        self.variables = []
        self.function_calls = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module if node.module else ""
        for alias in node.names:
            self.imports.append(f"{module}.{alias.name}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        for arg in node.args.args:
            self.variables.append(arg.arg)
        
        # Analyzing function calls within functions
        FunctionCallVisitor(self.function_calls).visit(node)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        class_info = {"name": node.name, "methods": []}
        self.classes.append(class_info)
        
        for body_item in node.body:
            if isinstance(body_item, ast.FunctionDef):
                class_info["methods"].append(body_item.name)
                self.variables.extend(arg.arg for arg in body_item.args.args)
                
                # Analyze function calls within methods
                FunctionCallVisitor(self.function_calls).visit(body_item)
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            self.variables.append(node.targets[0].id)
        self.generic_visit(node)

