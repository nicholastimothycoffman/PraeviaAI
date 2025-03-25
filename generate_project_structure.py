import os

EXCLUDED_DIRS = {'.git', 'venv', '__pycache__', '.DS_Store'}
OUTPUT_FILE = "project_structure.md"

def generate_structure(path='.', prefix=''):
	lines = []

	for item in sorted(os.listdir(path)):
		if item in EXCLUDED_DIRS:
			continue

		full_path = os.path.join(path, item)

		if os.path.isdir(full_path):
			lines.append(f"{prefix} {item}/")
			lines.extend(generate_structure(full_path, prefix + "|  "))
		else:
			lines.append(f"{prefix} {item}")

	return lines

if __name__ == "__main__":
	structure = generate_structure(".")
	with open(OUTPUT_FILE, "w") as f:
		f.write("# Project Structure\n\n")
		f.write("\n".join(structure))

	print(f"Updated {OUTPUT_FILE}")
