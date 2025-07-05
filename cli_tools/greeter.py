# greeter.py

import click

@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.option(
    "-l",
    "--lang",
    help="Specify language English (en) or Spanish (es)",
    default="en",
    type=click.Choice(["en", "es"]),
)
@click.option(
    "--say-it",
    type=int,
    default=1,
    help="Number of times to say greeting",
)
def greet(first_name, last_name, lang, say_it):
    """Displays a greeting to the user."""
    greetings = "Hello" if lang == "en" else "Hola"
    for _ in range(say_it):
        click.secho(f'{greetings} {first_name} {last_name}!', fg="red", bg="white")
