# Readme Doctor

A Python-powered AI assistant for rapid generation and refinement of GitHub READMEs, purpose-built for hackathons and agile development cycles.

## Key Features

*   AI-powered README generation from essential project inputs.
*   Intelligent polishing and enhancement of existing README files.
*   Two distinct operational modes: Generate and Polish, optimized for speed.
*   Leverages Google Gemini AI for producing high-quality, relevant text.
*   Designed to significantly reduce documentation overhead in time-constrained environments.

## How It Works

The `main.py` script serves as the central interface for Readme Doctor. When executed without any command-line arguments, it initiates "Generate" mode, prompting the user for core project details such as name, description, and key modules. These inputs are then dispatched to the integrated Google Gemini AI.

Alternatively, when `main.py` is invoked with a file path argument (e.g., `python main.py my_readme.md`), it activates "Polish" mode. The script reads the specified README content, submits it to the Gemini AI for analysis and enhancement, and then returns an improved version.

In both operational modes, the AI processes the provided input, constructs or refines the README, and the script saves the resulting Markdown file directly to the project's root directory.

## Installation / Usage

Readme Doctor requires Python 3.8 or newer.

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/readme-doctor.git # Replace with actual repo URL
cd readme-doctor
pip install -r requirements.txt
```

Ensure your Gemini API key is configured. This is typically done by setting the `GEMINI_API_KEY` environment variable.

### Generate Mode

To create a new README from scratch, execute the script without any arguments:

```bash
python main.py
```

Follow the interactive prompts to provide your project's name, a brief description, and any relevant modules or technologies. The generated README will be saved as `generated_README.md` in your current directory.

### Polish Mode

To enhance an existing README file, pass its path as a command-line argument:

```bash
python main.py current_readme.md
```

The script will read, process, and then save the polished README as `polished_README.md` in your current directory.

## Example Usage

### Generating a New README

```bash
# Execute the script to enter interactive generation
python main.py

# Script prompts for information:
# Enter Project Name: Event Planner
# Enter Project Description: A web application for scheduling and managing events.
# Enter Key Modules (comma-separated): Flask, SQLAlchemy, Celery, React
#
# (Output: A new file named 'generated_README.md' is created with comprehensive content.)
```

### Polishing an Existing README

Assume you have a file named `draft_project_readme.md` in your current directory.

```bash
# Polish the existing README file
python main.py draft_project_readme.md

# (Output: A new file named 'polished_README.md' is created, containing the enhanced content.)
```
### Demo
Watch demo on YouTube: https://youtu.be/J3C4FNUVDxg?si=MB91iSGtxoiHdwtd

## Project Structure
```bash
readme-doctor/
├── generator.py
├── generate.py
├── polish.py
├── prompts.py
├── main.py
```

### File Breakdown

* `generator.py`
Handles all communication with the Gemini API.
This file is responsible for sending prompts, managing API requests, and returning generated text.

* `generate.py`
Implements Generate Mode.
Collects structured project details (project name, description, modules), and produces a complete README from scratch.

* `polish.py`
Implements Polish Mode.
Takes an existing README file and refines it into a concise, professional, hackathon-ready version.

* `prompts.py`
Stores all prompt templates used by the application.
Separating prompts keeps generation logic clean and makes prompt iteration easier.

* `main.py`
Entry point of the application.
Handles CLI arguments, determines whether to run Generate or Polish mode, and orchestrates the full pipeline.

This modular structure keeps API logic, prompt design, and execution flow clearly separated, making the tool easy to extend and maintain.

## Future Improvements

*   Direct integration with various version control platforms for seamless README updates.
*   Support for a wider range of AI models and API providers, offering choice and redundancy.
*   Advanced customization options for README sections, structure, and stylistic preferences.
*   Command-line interface (CLI) arguments for non-interactive operations, improving automation workflows.
*   Enhanced context awareness for more nuanced and project-specific documentation.

## License

This project is licensed under the MIT License.


This README was generated using README Doctor.
