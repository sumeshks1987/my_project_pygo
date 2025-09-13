import requests
import csv
from time import sleep

POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon'
OUTPUT_FILE = 'pokedex_data.csv'  # Save to this file

def get_pokemon_list(limit=150):
    url = f"{POKEAPI_URL}?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [pokemon['url'] for pokemon in data['results']]

def get_pokemon_details(pokemon_url):
    response = requests.get(pokemon_url)
    response.raise_for_status()
    data = response.json()

    types = [t['type']['name'] for t in data['types']]
    abilities = [a['ability']['name'] for a in data['abilities']]
    moves = [m['move']['name'] for m in data['moves']]

    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

    return {
        'id': data['id'],
        'name': data['name'],
        'base_experience': data['base_experience'],
        'height': data['height'],
        'weight': data['weight'],
        'types': ', '.join(types),
        'abilities': ', '.join(abilities),
        'moves': ', '.join(moves),
        'hp': stats.get('hp', 0),
        'attack': stats.get('attack', 0),
        'defense': stats.get('defense', 0),
        'special-attack': stats.get('special-attack', 0),
        'special-defense': stats.get('special-defense', 0),
        'speed': stats.get('speed', 0),
    }

def main():
    print("Fetching list of Pokémon...")
    pokemon_urls = get_pokemon_list(limit=150)  # You can increase this limit if needed

    print(f"Fetching details for {len(pokemon_urls)} Pokémon...")
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = [
            'id', 'name', 'base_experience', 'height', 'weight',
            'types', 'abilities', 'moves',
            'hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed'
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for idx, url in enumerate(pokemon_urls, start=1):
            try:
                details = get_pokemon_details(url)
                writer.writerow(details)
                print(f"[{idx}/{len(pokemon_urls)}] Fetched {details['name']}")
                sleep(0.2)  # Be polite to the API
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")

    print(f"\n✅ Complete dataset saved to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
