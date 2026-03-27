"""Simple CLI app — clean code for poetry/flat security audit testing."""
import click
from rich.console import Console

console = Console()


@click.command()
@click.option("--name", default="world", help="Name to greet.")
def greet(name: str) -> None:
    """Greet the user."""
    console.print(f"[bold]Hello, {name}![/bold]")


if __name__ == "__main__":
    greet()
