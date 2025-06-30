# authenticate.py

import click

@click.command()
@click.option("--username", prompt=True)
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
def auth(username, password):
    """Provides user authentication"""
    click.echo(f"Logging in as {username}")


@click.command()
def login():
    """Provides login start"""
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True, confirmation_prompt=True)
    if click.confirm("Are you an admin?"):
        admin_id = click.prompt("Admin ID", type=int, prompt_suffix=">")
        click.echo(f"Logging in admin {username} (ID = {admin_id})")
    else:
        click.echo(f"You are now logged in as {username}")

