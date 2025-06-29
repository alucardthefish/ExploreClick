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
def greet(first_name, last_name, lang):
    """Displays a greeting to the user."""
    greetings = "Hello" if lang == "en" else "Hola"
    click.echo(f'{greetings} {first_name} {last_name}!')
