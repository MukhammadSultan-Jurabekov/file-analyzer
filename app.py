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
        
