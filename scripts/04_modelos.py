"""
04_modelos.py
Modelos predictivos del total final tras cada prueba (1 a 9) y evaluación.

Entrada: data/processed/decatlones_limpio.csv, data/processed/perfiles.csv
Salida:  data/processed/mae_por_prueba.csv
"""

import logging
from pathlib import Path

# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.metrics import mean_absolute_error

RAIZ = Path(__file__).resolve().parents[1]
PROCESSED = RAIZ / "data" / "processed"
LOGS = RAIZ / "logs"

UMBRAL_FIABLE = 100  # puntos de MAE

logging.basicConfig(
    filename=LOGS / "04_modelos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    # 1. División temporal: entrenamiento 2014-2022, evaluación 2023-2025

    # 2. Para cada prueba k de 1 a 9:
    #    - regresión lineal y KNN con los puntos acumulados (con y sin perfil)
    #    - referencia ingenua: extrapolar los puntos acumulados
    #    - referencia de potencial: suma de mejores marcas de la temporada
    #    - calcular el MAE de cada uno

    # 3. Prueba a partir de la cual el MAE < UMBRAL_FIABLE

    # 4. Guardar resultados en data/processed/mae_por_prueba.csv
    pass


if __name__ == "__main__":
    main()
