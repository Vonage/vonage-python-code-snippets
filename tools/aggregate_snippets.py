from collections import defaultdict
import os
from typing import DefaultDict


def extract_relevant_lines(content_lines: list[str]) -> tuple[int, int]:
    """
    Extract the relevant line numbers from a Python file.
    Uses same logic as update_python_snippet_line_numbers.py from "content-repo".
    """
    start_line = 0
    end_line = len(content_lines)

    # Check for FastAPI
    for line in content_lines:
        if line.startswith('from fastapi import'):
            return start_line, end_line

    # Find Vonage import
    for i, line in enumerate(content_lines):
        if line.startswith('from vonage import Auth, Vonage'):
            start_line = i
            break

    return start_line, end_line


def get_display_title(snippet_title: str, directory: str) -> str:
    """
    Generate a display title for a snippet.
    If the file is main.py, use the parent directory name instead.
    """
    if snippet_title.startswith(directory + '/'):
        display_title = snippet_title[len(directory) + 1 :]
    else:
        display_title = snippet_title

    # Check if this is a main.py file
    parts = display_title.split('/')
    if parts[-1] == 'main':
        if len(parts) > 1:
            display_title = parts[-2]  # Use parent directory name
        else:
            display_title = directory  # Fallback to top dir if no parent

    # Format for display
    display_title = display_title.replace('/', ' ').replace('-', ' ').title()
    return display_title


def main():
    """
    This script aggregates all the snippets from the content-repo into a single file.
    It recursively navigates through all folders that don't start with a dot,
    finds .py files, and adds their contents to the markdown file.

    It should be run from the root directory of the code snippets repo.
    """

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_file = os.path.join(repo_root, 'SNIPPETS.md')
    snippets_by_directory: DefaultDict[str, dict[str, str]] = defaultdict(dict)

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        if os.path.basename(root) in {'tools', 'meetings', 'number-insight-v2'}:
            continue

        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, repo_root)

                parts = relative_path.split(os.sep)
                if len(parts) > 1:
                    top_dir = parts[0]
                    snippet_title = relative_path[:-3]

                try:
                    with open(file_path, 'r') as f:
                        snippet_lines = f.readlines()
                        start_line, end_line = extract_relevant_lines(snippet_lines)

                        relevant_content = ''.join(snippet_lines[start_line:end_line])

                        snippets_by_directory[top_dir][snippet_title] = relevant_content
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    with open(output_file, 'w') as f:
        f.write('## Python Code Snippets\n\n')
        f.write(
            'This is a list of all supported Python code snippets in the repo, organised by category.\n\n'
        )

        # Table of contents
        f.write('### Table of Contents\n\n')
        for directory in sorted(snippets_by_directory.keys()):
            f.write(f'- [{directory.title().replace("-", " ")}](#{directory})\n')
        f.write('\n')

        # Table of contents for each section
        for directory in sorted(snippets_by_directory.keys()):
            dir_snippets = snippets_by_directory[directory]
            dir_title = directory.title().replace('-', ' ')

            f.write(f'### {dir_title}\n\n')
            f.write(f'#### Snippets in this Section\n\n')

            for snippet_title in sorted(dir_snippets.keys()):
                display_title = get_display_title(snippet_title, directory)
                snippet_link = display_title.lower().replace(' ', '-')
                f.write(f'- [{display_title}](#{snippet_link})\n')

            f.write('\n')

            # Individual snippets
            for snippet_title in sorted(dir_snippets.keys()):
                display_title = get_display_title(snippet_title, directory)

                f.write(f'#### {display_title}\n\n')
                f.write('```python\n')
                f.write(dir_snippets[snippet_title])
                if not dir_snippets[snippet_title].endswith('\n'):
                    f.write('\n')
                f.write('```\n\n')

    print(f"Successfully generated {output_file}")
    print(f"Found snippets in {len(snippets_by_directory)} top-level directories")
    total_snippets = sum(len(snippets) for snippets in snippets_by_directory.values())
    print(f"Total snippets: {total_snippets}")

    # Add snippets to the readme
    with open('readme-base.md', 'r') as readme_base_file:
        readme_base = readme_base_file.read()

    with open('SNIPPETS.md') as snippets_file:
        snippets_base = snippets_file.read()

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_base)
        readme_file.write('\n\n')
        readme_file.write(snippets_base)


if __name__ == '__main__':
    main()
