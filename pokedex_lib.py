import pandas as pd

DATA_FILE = 'pokedex_data.csv'

def load_data():
    return pd.read_csv(DATA_FILE)

def search_pokemon(name):
    df = load_data()
    return df[df['name'].str.contains(name, case=False, na=False)]

def filter_by_type(poke_type):
    df = load_data()
    return df[(df['type1'].str.lower() == poke_type.lower()) | (df['type2'].str.lower() == poke_type.lower())]

def export_pokemon(poke_type, output_file):
    filtered = filter_by_type(poke_type)
    filtered.to_csv(output_file, index=False)
