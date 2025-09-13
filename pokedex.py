import click
from pokedex_lib import search_pokemon, filter_by_type, export_pokemon

@click.group()
def cli():
    """Pokémon CLI - Search and filter Pokémon data."""
    pass

@click.command()
@click.option('--name', help='Search Pokémon by name (partial allowed).')
def search(name):
    results = search_pokemon(name)
    if results.empty:
        click.echo("No Pokémon found with that name.")
    else:
        click.echo(results)

@click.command()
@click.option('--type', 'poke_type', help='Filter Pokémon by type (e.g., Fire, Water).')
def filter(poke_type):
    results = filter_by_type(poke_type)
    if results.empty:
        click.echo(f"No Pokémon found with type '{poke_type}'.")
    else:
        click.echo(results)

@click.command()
@click.option('--type', 'poke_type', help='Filter Pokémon by type to export.')
@click.option('--output', default='export/filtered_pokemon.csv', help='Output CSV file path.')
def export(type, output):
    export_pokemon(type, output)
    click.echo(f"Exported filtered Pokémon to {output}")

cli.add_command(search)
cli.add_command(filter)
cli.add_command(export)

if __name__ == '__main__':
    cli()
