import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .checker import scan_username

app = typer.Typer()
console = Console()


@app.command()
def main(
    username: str,
    deep: bool = typer.Option(False, "--deep", help="Enable deep scan"),
    strict: bool = typer.Option(False, "--strict", help="Enable strict mode"),
):
    console.print(Panel("VOIDSCAN", expand=True))

    mode = "normal"
    if deep:
        mode = "deep"
    elif strict:
        mode = "strict"

    console.print(f"[bold]Target:[/bold] {username}")
    console.print(f"[bold]Mode:[/bold] {mode}\n")

    results = scan_username(username, deep=deep, strict=strict)

    table = Table(title="Results")
    table.add_column("Site", style="cyan")
    table.add_column("Username", style="green")
    table.add_column("HTTP", justify="center")
    table.add_column("URL", overflow="fold")  # permite quebra de linha

    found_links = []

    for result in results:
        if result["status"] == 200:
            table.add_row(
                result["site"],
                result["username"],
                str(result["status"]),
                result["url"],
            )
            found_links.append(result["url"])

    console.print(table)

    # 🔥 Mostrar links completos abaixo
    if found_links:
        console.print("\n[bold]Full URLs:[/bold]\n")
        for link in found_links:
            console.print(link)

    console.print()


if __name__ == "__main__":
    app()
