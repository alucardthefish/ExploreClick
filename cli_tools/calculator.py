# calculator.py

import click


@click.command()
@click.argument('int_params', type=int, nargs=-1)
def add(int_params):
    """Adds numbers."""
    click.echo(sum(int_params))


@click.command()
@click.argument('int_params', type=int, nargs=-1)
def subtract(int_params):
    """Subtracts numbers."""
    results = int_params[0]
    for i in int_params[1:]:
        results -= i
    click.echo(results)
