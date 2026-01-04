from generate import generate_readme
from polish import polish_readme
import os
import sys

# Mode Handling
def main():
    if len(sys.argv) > 1:
        # Polish mode
        input_file = sys.argv[1]
        if not os.path.isfile(input_file):
            print(f"Error: {input_file} not found, ensure file is in root directory.")
            return
        polish_readme(input_file)
    else:
        # Generate mode
        generate_readme()


if __name__ == "__main__":
    main()
