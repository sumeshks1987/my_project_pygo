import click
import pandas as pd

DATA_FILE = 'pokedex_data.csv'

def load_data():
    return pd.read_csv(DATA_FILE)

@click.group()
def cli():
    """Pokémon CLI - Search and filter Pokémon data."""
    pass

@click.command()
@click.option('--name', help='Search Pokémon by name (partial match, case-insensitive).')
@click.option('--type', 'poke_type', help='Filter by type (e.g., Fire, Water).')
@click.option('--ability', help='Filter by ability (partial match, case-insensitive).')
@click.option('--min_attack', type=int, help='Minimum Attack stat filter.')
@click.option('--min_hp', type=int, help='Minimum HP stat filter.')
def search(name, poke_type, ability, min_attack, min_hp):
    df = load_data()

    if name:
        df = df[df['name'].str.contains(name, case=False, na=False)]
    if poke_type:
        df = df[df['types'].str.lower().str.contains(poke_type.lower())]
    if ability:
        df = df[df['abilities'].str.lower().str.contains(ability.lower())]
    if min_attack:
        df = df[df['attack'] >= min_attack]
    if min_hp:
        df = df[df['hp'] >= min_hp]

    if df.empty:
        click.echo("No Pokémon matched the search criteria.")
    else:
        click.echo(df[['id', 'name', 'types', 'abilities', 'hp', 'attack', 'defense']].to_string(index=False))

@click.command()
@click.option('--type', 'poke_type', help='Filter Pokémon by type to export.')
@click.option('--output', default='export/filtered_pokemon.csv', help='Output CSV file path.')
def export(type, output):
    df = load_data()
    if type:
        df = df[df['types'].str.lower().str.contains(type.lower())]

    df.to_csv(output, index=False)
    click.echo(f"Exported {len(df)} Pokémon to {output}")

cli.add_command(search)
cli.add_command(export)

if __name__ == '__main__':
    cli()
