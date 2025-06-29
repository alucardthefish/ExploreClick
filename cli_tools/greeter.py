# greeter.py

import click

@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.option(
    "--lang",
    help="Specify language English (en) or Spanish (es)",
    default="en"
)
def greet(first_name, last_name, lang):
    """Displays a greeting to the user."""
    if lang == "es":
        greetings = "Hola"
    elif lang == "en":
        greetings = "Hello"
    else:
        raise click.BadOptionUsage("lang", "lang must be 'en' or 'es'")
    click.echo(f'{greetings} {first_name} {last_name}!')
