import pandas as pd
from pathlib import Path
import urllib.request
import zipfile

# Création des dossiers
Path("data/raw").mkdir(parents=True, exist_ok=True)

url = "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20261012-171642/valeursfoncieres-2025.txt.zip"

zip_path = "data/raw/valeursfoncieres-2025.zip"

print("Téléchargement...")
urllib.request.urlretrieve(url, zip_path)

print("Décompression...")
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall("data/raw")

print("Lecture du fichier...")

txt_file = "data/raw/valeursfoncieres-2025.txt"

df = pd.read_csv(
    txt_file,
    sep="|",
    low_memory=False
)

print(f"{len(df):,} lignes chargées")

print("Conversion en parquet...")

df.to_parquet(
    "data/raw/valeursfoncieres-2025.parquet",
    index=False
)

print("Terminé")