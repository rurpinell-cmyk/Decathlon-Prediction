"""
01_scraping.py
Descarga los resultados de decatlones (World Athletics, Decathlon2000.com)
y los guarda SIN MODIFICAR en data/raw/.

Entrada: URLs de las competiciones (2014-2025, masculino)
Salida:  data/raw/resultados_raw.csv
"""

import logging
from pathlib import Path

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"
LOGS = RAIZ / "logs"

# Registro de ejecución en /logs (páginas fallidas, etc.)
logging.basicConfig(
    filename=LOGS / "01_scraping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def descargar_competicion(url):
    """Descarga y procesa una página de resultados. Devuelve una lista de filas."""
    # TODO: requests.get(url) + BeautifulSoup para leer la tabla
    pass


def main():
    urls = []  # TODO: lista de URLs de competiciones
    filas = []

    for url in urls:
        # try/except: si una página falla, se registra y se sigue con la siguiente
        try:
            filas.extend(descargar_competicion(url))
            logging.info(f"OK: {url}")
        except Exception as e:
            logging.warning(f"Página fallida: {url} - {e}")

    # TODO: pd.DataFrame(filas).to_csv(RAW / "resultados_raw.csv", index=False)


if __name__ == "__main__":
    main()
