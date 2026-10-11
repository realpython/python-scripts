"""Read-only MCP tools for discovering and inspecting repository scripts."""

from __future__ import annotations

import ast
import json
import warnings
from pathlib import Path

from mcp.server.mcpserver import MCPServer


SCRIPTS_DIR = (Path(__file__).resolve().parent / "scripts").resolve()
server = MCPServer(
    name="python-scripts",
    version="1.0.0",
    description=(
        "Read-only catalog and source access for this repository's "
        "Python scripts."
    ),
)


def _script_path(filename: str) -> Path:
    """Return a validated Python script path inside the scripts directory."""
    if Path(filename).name != filename or not filename.endswith(".py"):
        raise ValueError(
            "Provide the filename of a Python script in the scripts directory."
        )

    path = (SCRIPTS_DIR / filename).resolve()
    if path.parent != SCRIPTS_DIR or not path.is_file():
        raise FileNotFoundError(f"Python script not found: {filename}")
    return path


@server.tool(
    description=(
        "List Python utility scripts in the repository, with their module "
        "docstrings when available."
    )
)
def list_scripts() -> str:
    """Return a JSON catalog of Python utility scripts."""
    catalog = []
    for path in sorted(SCRIPTS_DIR.glob("*.py")):
        try:
            source = path.read_text(encoding="utf-8")
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                description = ast.get_docstring(ast.parse(source)) or ""
        except (OSError, SyntaxError, UnicodeError):
            description = ""
        catalog.append(
            {
                "filename": path.name,
                "description": (
                    description.splitlines()[0] if description else ""
                ),
            }
        )
    return json.dumps(catalog, ensure_ascii=False, indent=2)


@server.tool(
    description=(
        "Read the source of one Python script by filename. "
        "This does not execute the script."
    )
)
def read_script(filename: str) -> str:
    """Return a script's UTF-8 source without executing it."""
    return _script_path(filename).read_text(encoding="utf-8")


if __name__ == "__main__":
   rem repeat server.run(transport="stdio")
