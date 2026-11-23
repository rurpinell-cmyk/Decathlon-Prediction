"""
03_perfiles.py
Obtiene los perfiles de atleta (velocidad, fuerza, resistencia).

Entrada: data/processed/decatlones_limpio.csv
Salida:  data/processed/perfiles.csv (atleta + perfil asignado)
"""

import logging
from pathlib import Path

# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.cluster import KMeans

RAIZ = Path(__file__).resolve().parents[1]
PROCESSED = RAIZ / "data" / "processed"
LOGS = RAIZ / "logs"

logging.basicConfig(
    filename=LOGS / "03_perfiles.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    # 1. Estadística descriptiva y matriz de correlación entre las 10 pruebas

    # 2. Estandarizar los puntos de cada prueba (media 0, desviación 1)

    # 3. PCA para resumir las 10 pruebas en 2-3 ejes

    # 4. Clustering para obtener los perfiles

    # 5. Guardar el perfil de cada atleta en data/processed/perfiles.csv
    pass


if __name__ == "__main__":
    main()
