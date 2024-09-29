# Python Code Analysis Script

This is a simple Python script that analyzes the structure and composition of a Python file, providing detailed information about functions, classes, imports, variables, and function calls.

## Features

- Extracts and lists all **imported modules**.
- Identifies all **functions** defined in the file.
- Detects all **classes** and their **methods**.
- Extracts all **variables** used in functions and classes.
- Displays all **function calls** made within the file.

## Prerequisites

- **Python 3** installed on your system.
- `pip3` (although no additional packages are required for this script, you need Python 3 and pip3 to be installed correctly).

## How to Use

1. **Clone or download the script**: Save the script file as `analyze_python.py` to your local system.

2. **Run the script**:
   Open your terminal or command prompt, navigate to the directory where `analyze_python.py` is located, and execute:

 ```
   python3 analyze_python.py
```


Provide the file path: When prompted, enter the path to the Python file you want to analyze. For example:

```
Enter the path to the Python file to analyze: /path/to/your/code.py

```
View the analysis output: The script will display detailed information about the analyzed file, including:

- Imported modules
- Functions and their arguments
- Classes and their methods
- Variables used in the code
- Function calls made within the code

## Example
If you have a Python file example.py with the following content:

```


import os
import sys

class SampleClass:
    def __init__(self):
        self.name = "example"

    def greet(self):
        print("Hello, World!")

def sample_function(arg1, arg2):
    result = arg1 + arg2
    return result

```
The analysis output will look like this:

```
Imports:
  - os
  - sys

Functions:
  - sample_function

Classes:
  - SampleClass
    - Method: __init__
    - Method: greet

Variables:
  - self
  - name
  - arg1
  - arg2
  - result

Function Calls:
  - print

```
## Troubleshooting

Make sure you have Python 3 installed by running  ```python3 --version.```
Ensure that the file you want to analyze exists and that you have read permissions for it.

This script uses Python's built-in ast module, so no additional packages need to be installed.
Works on any platform where Python 3 is available (Linux, macOS, Windows).

