import pathlib
import re
import subprocess
import urllib.parse
from griffe2md.cli import main as griffe2md_cli  # type: ignore


def get_git_remote_url() -> str:
    """Get the git remote origin URL."""
    try:
        result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def parse_github_url(git_url: str) -> str:
    """Convert git URL to GitHub base URL for source browsing."""
    if not git_url:
        return ""

    parsed_url = urllib.parse.urlparse(git_url)

    # it should work for ssh and https and any git hosting service
    host_name = parsed_url.netloc
    path = parsed_url.path.lstrip("/").replace(".git", "")
    return f"https://{host_name}/{path}/blob/main"


def get_source_file_path(module_path: str) -> str:
    """Convert module path to source file path."""
    # Convert src.package.hello.hello_world -> src/package/hello.py
    parts = module_path.split(".")
    if len(parts) > 1:
        # Remove 'src' prefix and reconstruct path
        file_parts = parts[1:]  # Skip 'src'
        if len(file_parts) == 1:
            # Module level: src.package -> src/package/__init__.py
            return f"src/{'/'.join(file_parts)}/__init__.py"
        elif len(file_parts) == 2:
            # Submodule level: src.package.hello -> src/package/hello.py
            return f"src/{file_parts[0]}/{file_parts[1]}.py"
        else:
            # Function level: src.package.hello.hello_world -> src/package/hello.py
            # Functions are in the same file as their parent module
            return f"src/{file_parts[0]}/{file_parts[1]}.py"
    return ""


def get_src_packages(src_path: pathlib.Path) -> list[pathlib.Path]:
    """Get all Python packages in the src directory."""
    packages = []
    for item in src_path.iterdir():
        if item.is_dir() and not item.name.startswith("__") and not item.name.startswith("."):
            # Check if it's a Python package (has __init__.py)
            if (item / "__init__.py").exists():
                packages.append(item)
    return packages


def get_griffe_docs(module_path: str, out_path: pathlib.Path) -> None:
    """Generate griffe documentation for a specific module."""
    griffe2md_cli([module_path, "-o", str(out_path)])


def get_frontmatter(title: str, sidebar_label: str) -> str:
    """Generate frontmatter for markdown files."""
    return f"---\ntitle: {title}\nsidebar_label: {sidebar_label}\n---\n\n"


def clean_generated_markdown(content: str, github_base_url: str = "") -> str:
    """Clean up the generated markdown content and replace links with GitHub URLs."""
    # Remove empty descriptions (links ending with " –" or " -")
    content = re.sub(r"\[(.*?)\]\(([^)]+)\) –\s*$", r"[\1](\2)", content, flags=re.MULTILINE)
    content = re.sub(r"\*\*(.*?)\*\*\]\(([^)]+)\) –\s*$", r"**\1**](\2)", content, flags=re.MULTILINE)

    # Replace internal anchor links with GitHub source links
    if github_base_url:

        def replace_link(match: re.Match[str]) -> str:
            link_text = match.group(1)
            anchor = match.group(2)

            # Extract module path from anchor (e.g., #src.package.hello.hello_world)
            if anchor.startswith("#src."):
                module_path = anchor[1:]  # Remove #
                source_file = get_source_file_path(module_path)
                if source_file:
                    github_url = f"{github_base_url}/{source_file}"
                    return f"[{link_text}]({github_url})"

            # Keep original link if we can't parse it
            return match.group(0)

        content = re.sub(r"\[(.*?)\]\((#[^)]+)\)", replace_link, content)
        content = re.sub(r"\*\*(.*?)\*\*\]\((#[^)]+)\)", replace_link, content)

    # Fix example code blocks - make them proper code blocks
    content = re.sub(
        r'<details class="example"[^>]*>\s*<summary>Example</summary>\s*(.*?)\s*</details>',
        lambda m: f"\n**Example:**\n\n```python\n{m.group(1).strip()}\n```\n",
        content,
        flags=re.DOTALL,
    )

    # Clean up module headings - remove "src." prefix for cleaner look
    content = re.sub(r"^## src\.", "## ", content, flags=re.MULTILINE)
    content = re.sub(r"^### src\.", "### ", content, flags=re.MULTILINE)
    content = re.sub(r"^#### src\.", "#### ", content, flags=re.MULTILINE)

    # Remove unnecessary "Modules:" and "Functions:" headers if they're followed by empty content
    content = re.sub(r"\*\*Modules:\*\*\s*\n\s*\n", "", content)
    content = re.sub(r"\*\*Functions:\*\*\s*\n\s*\n", "", content)

    # Clean up extra whitespace
    content = re.sub(r"\n{3,}", "\n\n", content)

    # Fix type links that look ugly
    content = re.sub(r"<code>\[([^\]]+)\]\([^)]+\)</code>", r"`\1`", content)

    return content.strip()


def build_reference_docs() -> None:
    """Build reference documentation for all packages in src."""
    src_path = pathlib.Path("src")
    out_base = pathlib.Path("docs/astro/src/content/docs/api")

    # Get GitHub base URL for source links
    git_url = get_git_remote_url()
    github_base_url = parse_github_url(git_url)

    if github_base_url:
        print(f"Will link to source code at: {github_base_url}")
    else:
        print("No valid git remote found, using internal links")

    # Create output directory
    out_base.mkdir(parents=True, exist_ok=True)

    # Get all packages in src
    packages = get_src_packages(src_path)

    if not packages:
        print("No Python packages found in src directory")
        return

    # Generate an index file for the API documentation
    index_content = get_frontmatter("API Reference", "API")
    index_content += "# API Reference\n\n"
    index_content += "This section contains the API documentation for all packages.\n\n"
    index_content += "## Packages\n\n"

    for package in packages:
        package_name = package.name
        package_title = package_name.replace("_", " ")

        # Add to index
        index_content += f"- [{package_title}](./{package_name}/) - Documentation for the {package_name} package\n"

        # Create package-specific documentation
        package_out_dir = out_base / package_name
        package_out_dir.mkdir(exist_ok=True)

        # Generate docs for this specific package
        module_path = f"src.{package_name}"
        package_out_file = package_out_dir / "index.md"

        try:
            # Generate the documentation
            get_griffe_docs(module_path, package_out_file)

            # Read the generated content, clean it, and add frontmatter
            if package_out_file.exists():
                content = package_out_file.read_text()
                # Clean up the generated markdown and replace links
                cleaned_content = clean_generated_markdown(content, github_base_url)
                frontmatter = get_frontmatter(f"{package_title} API", package_title)
                package_out_file.write_text(frontmatter + cleaned_content + "\n")

            print(f"Generated documentation for {package_name}")

        except Exception as e:
            print(f"Error generating documentation for {package_name}: {e}")

    # Write the index file
    index_file = out_base / "index.mdx"
    index_file.write_text(index_content)
    print(f"Generated API index at {index_file}")


if __name__ == "__main__":
    build_reference_docs()
