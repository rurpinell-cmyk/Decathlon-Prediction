# ¿Cuándo se decide un decatlón?

Predicción en directo de la puntuación final de un decatlón según el perfil del atleta.

Caso práctico de la asignatura **Programación y Análisis de Datos Deportivos** (Máster en Análisis de Datos Deportivos, URJC).
Autor: Robert Urpinell Aynés.

## Objetivo

Predecir los puntos totales con los que acabará cada decatleta a partir de los resultados acumulados tras cada prueba, y averiguar a partir de qué prueba la predicción es fiable (MAE < 100 puntos). Se comprueba además si añadir el perfil del atleta (velocidad, fuerza, resistencia), obtenido con clustering, mejora la predicción.

## Datos

- Resultados oficiales de World Athletics (webscraping).
- Histórico de Decathlon2000.com.
- Dataset `decathlon` del paquete FactoMineR (para construir y probar el proceso).
- Tablas de puntuación de World Athletics (coeficientes).

Alcance: decatlones masculinos 2014-2025. Los datos **no se suben al repositorio** (ver `.gitignore`); se generan ejecutando los scripts.

## Estructura del repositorio

```
decatlon-prediccion/
├── data/
│   ├── raw/          # datos originales descargados (no se modifican nunca)
│   └── processed/    # datos limpios, generados por los scripts
├── scripts/
│   ├── 01_scraping.py    # descarga de resultados
│   ├── 02_limpieza.py    # limpieza, validaciones y variables derivadas
│   ├── 03_perfiles.py    # estandarización, PCA y clustering
│   └── 04_modelos.py     # modelos predictivos y evaluación
├── reports/
│   ├── caso_practico.qmd         # documento del caso práctico (Quarto)
│   └── estructura_repositorio.png
├── logs/             # registros de ejecución (no se suben)
├── requirements.txt
└── README.md
```

## Cómo reproducirlo

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar los scripts en orden
python scripts/01_scraping.py
python scripts/02_limpieza.py
python scripts/03_perfiles.py
python scripts/04_modelos.py

# 3. Generar el documento del caso práctico
quarto render reports/caso_practico.qmd
```

## Metodología (resumen)

1. Descriptiva y matriz de correlación entre pruebas.
2. Estandarización + PCA (2-3 ejes) + clustering → perfiles de atleta.
3. Tras cada prueba (1 a 9): regresión lineal y KNN.
4. Evaluación con división temporal (entrenamiento 2014-2022, test 2023-2025) y MAE.
5. Comparación con dos referencias: ingenua (extrapolar puntos acumulados) y de potencial (suma de mejores marcas de la temporada).

## Estado

- [ ] Scraping
- [ ] Limpieza
- [ ] Perfiles
- [ ] Modelos
- [ ] Informe
