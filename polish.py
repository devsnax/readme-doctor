from generator import readme_generator
from prompts import polish_prompt

def polish_readme(input_file: str, output_file: str = "polished_README.md"):
    with open(input_file, "r") as f:
        old_text = f.read()
    
    print("\nPolishing README...")
    refined_text = readme_generator(polish_prompt(old_text))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(refined_text)

    print(f"Polished README saved as {output_file}")