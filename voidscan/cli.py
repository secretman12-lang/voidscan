import asyncio
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .checker import deep_scan

app = typer.Typer()
console = Console()

@app.command()
def scan(
    username: str,
    strict: bool = typer.Option(False, "--strict", help="Strict mode (accurate, fewer results)"),
    deep: bool = typer.Option(False, "--deep", help="Deep mode (variations + broader scan)")
):

    mode = "normal"
    if strict:
        mode = "strict"
    if deep:
        mode = "deep"

    console.print(Panel("VOIDSCAN", style="cyan"))
    console.print(f"Target: {username}")
    console.print(f"Mode: {mode}\n")

    results = asyncio.run(deep_scan(username, mode))

    found = [r for r in results if r["exists"]]

    table = Table(title="Results")
    table.add_column("Site")
    table.add_column("Username")
    table.add_column("HTTP")
    table.add_column("URL")

    for r in found:
        table.add_row(
            r["site"],
            r["username"],
            str(r["status"]),
            r["url"]
        )

    if found:
        console.print(table)
    else:
        console.print("[red]No profiles found.[/red]")

if __name__ == "__main__":
    app()
