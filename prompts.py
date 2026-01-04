# Prompt for polishing existing README
def polish_prompt(old_text):
    return f"""
    You are a professional open-source technical writer.

    TASK:
    Rewrite and polish the README content provided below to be hackathon-ready.

    STRICT RULES:
    - Return ONLY the final README content. DO NOT INCLUDE STARTING TEXT, ONLY RETURN THE FINAL OUTPUT!
    - Do NOT include emojis.
    - Do NOT include explanations, commentary, analysis, introductions, or conclusions.
    - Do NOT include blocks like "Future Enhancements" or "Team"
    - Work with ONLY what is included in the README
    - Do NOT include phrases like:
    "This is a great starting point"
    "Here's a refined version"
    "Let's improve"
    - Do NOT wrap the output in quotes.
    - Do NOT use markdown separators like "---" unless they belong inside the README itself.
    - Output must start immediately with the README content (e.g. a title or badge).

    STYLE REQUIREMENTS:
    - Concise, confident, developer-focused
    - Clear value proposition
    - Hackathon-grade clarity
    - No generic AI filler language

    README to polish:
    {old_text}

    If examples are included, they MUST be generic and clearly marked as examples.
    Do NOT assume specific repo structure.
    Return only the README text, do NOT respond with irrelevant text as your output is to be used directly in production.
    """.strip()


# Prompt for new README
def generate_prompt(project_name, description, modules):
    return f"""
You are a senior developer creating a hackathon-ready README for an open-source project.

STRICT OUTPUT RULES:
- Do NOT include emojis.
- Output ONLY a complete README.md
- No explanations, no commentary, no prefaces
- No phrases like "Below is", "Here’s", "This project"
- Start directly with the README title

README MUST INCLUDE:
- Project title
- One-sentence elevator pitch
- Key features (bullet points)
- How it works (high-level)
- Installation / Usage
- Example usage (generic, not repo-specific)
- Future improvements
- License section

TONE:
- Confident
- Practical
- Clean
- Non-generic
- Hackathon-quality

PROJECT DETAILS:
Project name: {project_name}
Description: {description}
Modules: {modules}

Return only the README text, do NOT respond with irrelevant text as your output is to be used directly in production.
If examples are included, they MUST be generic and clearly marked as examples.
Do NOT assume specific repo structure.
""".strip()