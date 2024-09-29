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

    def report(self):
        print("Imports:")
        for imp in self.imports:
            print(f"  - {imp}")
        
        print("\nFunctions:")
        for func in self.functions:
            print(f"  - {func}")

        print("\nClasses:")
        for cls in self.classes:
            print(f"  - {cls['name']}")
            for method in cls["methods"]:
                print(f"    - Method: {method}")

        print("\nVariables:")
        for var in set(self.variables):
            print(f"  - {var}")

        print("\nFunction Calls:")
        for call in self.function_calls:
            print(f"  - {call}")

class FunctionCallVisitor(ast.NodeVisitor):
    def __init__(self, function_calls):
        self.function_calls = function_calls

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.function_calls.append(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            self.function_calls.append(f"{ast.unparse(node.func)}")
        self.generic_visit(node)

def analyze_python_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    try:
        tree = ast.parse(code)
        analyzer = PythonAnalyzer()
        analyzer.visit(tree)
        analyzer.report()
    except SyntaxError as e:
        print(f"Syntax error in file '{file_path}': {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the Python file to analyze: ").strip()
    analyze_python_file(file_path)
