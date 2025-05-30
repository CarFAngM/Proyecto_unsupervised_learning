import pandas as pd
from nba_api.stats.static import players
import os
from unidecode import unidecode

class NbaScraper:
    """Class to scrape NBA player information including headshot URLs."""

    @staticmethod
    def get_json_from_name(name: str) -> dict:
        nba_players = players.get_players()
        name_normalized = unidecode(name.lower())
        for player in nba_players:
            if unidecode(player['full_name'].lower()) == name_normalized:
                return player
        return None

    @staticmethod
    def get_headshot_url(player_id: int) -> str:
        return f'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png'


df = pd.read_excel("df_clusterizado.xlsx")  


df.columns = df.columns.str.strip()
print("Columnas disponibles:", df.columns.tolist())

name_column = 'name'

if name_column not in df.columns:
    raise KeyError(f"La columna '{name_column}' no existe. Revisa los nombres de columnas: {df.columns.tolist()}")


df['photo_url'] = None
df['player_id'] = None

for idx, row in df.iterrows():
    player_name = row.get(name_column)
    if not isinstance(player_name, str) or not player_name.strip():
        print(f"⚠️ Fila {idx} no tiene un nombre válido: {row}")
        continue

    player_info = NbaScraper.get_json_from_name(player_name)
    if player_info:
        player_id = player_info['id']
        headshot_url = NbaScraper.get_headshot_url(player_id)
        df.at[idx, 'player_id'] = player_id
        df.at[idx, 'photo_url'] = headshot_url
    else:
        print(f"❌ Jugador no encontrado: {player_name}")


output_file = "jugadores_nba_fotos_con_id.csv"
df.to_csv(output_file, index=False, encoding='utf-8')
print(f"✅ Archivo guardado en: {os.path.abspath(output_file)}")
