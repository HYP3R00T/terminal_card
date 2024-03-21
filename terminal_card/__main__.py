import argparse
from os import get_terminal_size
from pyfiglet import Figlet
from termcolor import cprint
from rich.console import Console
from rich.panel import Panel
from rich import print, box
from rich.panel import Panel


console = Console()


def handle_input():
    input()


try:
    width, height = get_terminal_size()
except:
    width, height = 80, 20


def main(text) -> None:
    with console.screen():
        brand = Figlet(font="big", justify="center", width=width)
        top_padding = int((height - 8 - 1 - 5 - 5) / 2)
        print("\n" * top_padding)
        cprint(brand.renderText("hyp3r00t"), color="blue", attrs=["bold"])
        print("\n")
        console.print(
            Panel.fit(
                f"[b blue]{text}",
                box=box.ROUNDED,
                padding=(1, 2),
                title="[b red]hyperoot.dev",
                border_style="red",
            ),
            justify="center",
        )
        print("\n\n")
        input()
    console.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide the title")
    parser.add_argument("text", type=str, help="Enter the title")
    args = parser.parse_args()
    main(args.text)
