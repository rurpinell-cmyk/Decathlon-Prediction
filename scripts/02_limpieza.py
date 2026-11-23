"""
02_limpieza.py
Limpia los datos originales y crea las variables derivadas.

Entrada: data/raw/resultados_raw.csv
Salida:  data/processed/decatlones_limpio.csv
"""

import logging
from pathlib import Path

# import pandas as pd
# import numpy as np

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"
PROCESSED = RAIZ / "data" / "processed"
LOGS = RAIZ / "logs"

logging.basicConfig(
    filename=LOGS / "02_limpieza.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    # 1. Leer data/raw/resultados_raw.csv

    # 2. Columna de estado (válida, nulo, DNF, DNS); nulo en concurso = 0 puntos

    # 3. Excluir decatlones incompletos y registrar cuántos se eliminan
    #    logging.info(f"Eliminados {n} decatlones incompletos")

    # 4. Normalizar unidades (m, s) y separador decimal

    # 5. Unificar nombres de atletas (tildes, mayúsculas)

    # 6. Variables derivadas:
    #    - puntos recalculados con la fórmula oficial
    #    - puntos acumulados y posición tras cada prueba
    #    - mejor total previo del atleta
    #    - referencia de potencial (suma de mejores marcas de la temporada)

    # 7. Validaciones:
    #    - puntos recalculados == puntos oficiales
    #    - total == suma de las 10 pruebas
    #    (las filas que no cumplan se registran en el log con el motivo)

    # 8. Guardar en data/processed/decatlones_limpio.csv
    pass


if __name__ == "__main__":
    main()
