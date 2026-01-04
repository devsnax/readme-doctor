from generator import readme_generator
from prompts import generate_prompt

def generate_readme(output_file: str = "output_readme.md"):
    print("\n––––––––––––––––––––––––––––––––––––––––––\n")
    print("\ \ \ \ \ \ \ README DOCTOR \ \ \ \ \ \ \ ")
    print("\n––––––––––––––––––––––––––––––––––––––––––\n")
    project_name = input("\nProject name: ").strip()
    description = input("\nShort description: ").strip()
    modules = input("\nModules used: ").strip()

    print("Generating README...")
    final_readme = readme_generator(generate_prompt(project_name, description, modules))

    with open(output_file, "w") as f:
        f.write(final_readme)

    print(f"Generated README saved as {output_file}")
