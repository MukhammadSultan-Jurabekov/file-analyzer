import ast
import os

class PythonAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = []
        self.functions = []
        self.classes = []
        self.variables = []
        self.function_calls = []
