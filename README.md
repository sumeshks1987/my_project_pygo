# Pokémon CLI

A command-line tool to search and filter Pokémon data.

## 🚀 Features

- Search Pokémon by name, type, ability, and stats.
- Combine multiple search filters for powerful queries.
- Export filtered Pokémon data to CSV.

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/pokemon-cli.git
cd pokemon-cli
pip install -r requirements.txt


🎯 Usage
✅ Search by Name
python pokedex.py search --name "Pikachu"

✅ Search by Type
python pokedex.py search --type "Fire"

✅ Search by Ability
python pokedex.py search --ability "chlorophyll"

✅ Search by Minimum Attack or HP
python pokedex.py search --min_attack 80 --min_hp 100

✅ Combine Multiple Filters
Example: Search Pokémon with type "Water", ability "torrent", and minimum attack of 50
python pokedex.py search --type "Water" --ability "torrent" --min_attack 50

✅ Export Filtered Pokémon to CSV
python pokedex.py export --type "Water" --output water_pokemon.csv