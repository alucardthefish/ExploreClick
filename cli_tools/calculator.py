# calculator.py

import click


def get_int_params_as_string(params: list[int]) -> list[str]:
    return [str(param) for param in params]


@click.command()
@click.argument('int_params', type=int, nargs=-1)
# @click.option("-v", "--verbose", is_flag=True, help="Show additional output.")
@click.option("-v", "--verbose", help="Show additional output.", count=True)
def add(int_params, verbose):
    """Adds numbers."""
    if verbose > 1:
        results = int_params[0]
        steps = [results]
        for x in int_params[1:]:
            steps.append(x)
            results += x
            click.echo(f"{' + '.join(get_int_params_as_string(steps))} = {sum(steps)}")
    elif verbose == 1:
        click.echo(f"{' + '.join(get_int_params_as_string(int_params))} = {sum(int_params)}")
    else:
        click.echo(sum(int_params))


@click.command()
@click.argument('int_params', type=int, nargs=-1)
# @click.option("-v", "--verbose", is_flag=True, help="Show additional output.")
@click.option("-v", "--verbose", help="Show additional output.", count=True)
def subtract(int_params, verbose):
    """Subtracts numbers."""
    if verbose > 1:
        z = int_params[0]
        steps = [z]
        for x in int_params[1:]:
            steps.append(x)
            z -= x
            click.echo(f"{' - '.join(get_int_params_as_string(steps))} = {z}")
    else:
        results = int_params[0]
        for i in int_params[1:]:
            results -= i
        if verbose:
            click.echo(f"{' - '.join(get_int_params_as_string(int_params))} = {results}")
        else:
            click.echo(results)
