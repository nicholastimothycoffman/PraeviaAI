import ast
import os
import inspect

OUTPUT_FILE = "docs/code_symbols.md"
EXCLUDED_DIRS = {'venv', '__pycache__', '.git', '.idea', '.DS_Store'}

def get_docstring_summary(node):
	if not ast.get_docstring(node):
		return ""
	doc = ast.get_docstring(node).split("\n")[0]
	return f" - *{doc}*"

def extract_symbols_from_file(filepath):
	with open(filepath, "r", encoding="utf-8") as f:
		source = f.read()
		tree = ast.parse(source)

	symbols = {"classes": [], "functions": []}
	for node in ast.walk(tree):
		if isinstance(node, ast.ClassDef):
			doc = get_docstring_summary(node)
			symbols["classes"].append(f"`class {node.name}`{doc}")
		elif isinstance(node, ast.FunctionDef):
			args = [arg.arg for arg in node.args.args]
			sig = f"{node.name}({', '.join(args)})"
			doc = get_docstring_summary(node)
			symbols["functions"].append(f"`def {sig}`{doc}")
	return symbols

def walk_project_structure(path="."):
	symbols_by_file = {}
	for root, _, files in os.walk(path):
		for f in files:
			if f.endswith(".py") and not any(ex in root for ex in EXCLUDED_DIRS):
				full_path = os.path.join(root, f)
				rel_path = os.path.relpath(full_path, path)
				symbols_by_file[rel_path] = extract_symbols_from_file(full_path)
	return symbols_by_file

def write_summary(symbols):
	with open(OUTPUT_FILE, "w") as f:
		f.write("# Code Symbols Index\n\n")
		for filepath, entries in symbols.items():
			f.write(f"## `{filepath}`\n")
			if entries["classes"]:
				f.write("- Classes:\n")
				for cls in entries["classes"]:
					f.write(f"  - {cls}\n")
			if entries["functions"]:
				f.write("- Functions:\n")
				for fn in entries["functions"]:
					f.write(f"  - {fn}\n")
			f.write("\n")

if __name__ == "__main__":
	symbols = walk_project_structure("app") # Start in the main codebase folder
	write_summary(symbols)
	print(f"Extracted to {OUTPUT_FILE}")	
