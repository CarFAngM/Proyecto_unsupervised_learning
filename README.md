# Análisis de Desempeño de Jugadores NBA mediante Aprendizaje No Supervisado

- Este proyecto realiza un análisis exploratorio de datos (EDA) y aplica técnicas de aprendizaje no supervisado (Unsupervised Learning) sobre datos de jugadores de la NBA. El objetivo es agrupar a los jugadores en clústers con base en su desempeño y características, y representar los hallazgos en un dashboard interactivo en Power BI.
- El proyecto fue desarrollado como parte del curso de Minería de Datos en la Universidad del Valle de Guatemala, correspondiente al ciclo académico 2025.

## Contenido: 

- Limpieza, transformación y escalamiento de datos.

## Análisis exploratorio:

- Distribución y tipo de variables.
- Relación entre métricas mediante correlaciones y gráficos.
- Tablas de contingencia y visualizaciones.

## Clusterización de jugadores:

- Aplicación de K-means y selección de K mediante el método del codo.
- Evaluación con coeficiente de silueta.
- Comparación con clustering jerárquico y visualización de dendograma.

## Análisis de los clústers resultantes:
- Asignación de nombres a clústers.
- Descripción de características comunes por grupo.

## Visualización:

- Dashboard interactivo en Power BI con información de rendimiento y clúster asignado para cada jugador.

## Estructura del repositorio: 

Archivos principales
- Proyecto Unsupervised Learning (NBA) - DMyML.Rmd
- Script principal en RMarkdown.
- Proyecto-Unsupervised-Learning--NBA----DMyML.html (Reporte HTML generado desde el Rmd)
- Proyecto final (Unsupervised learning) - Presentación.pdf (Presentación en PDF con resultados clave).

Dashboards en Power BI
- NBA Performance (Dashboard) - DMyML.pbix
- Dashboard principal en Power BI.
- Tablero Bi de los jugadores.pbix (Versión intermedia del dashboard).
- Presentación1.png (Fondo visual utilizado en el dashboard)

Datos
- df_scaled.csv / df_clusterizado.csv (Datos preprocesados y segmentados generados en el rmd).

- df2.xlsx / nba_players_2023_clustering (1).csv (Dataset original y dataset procesado utilizado para analisis de clusters).

- jugadores_nba_fotos.csv / jugadores_nba_fotos_con_id.csv (Dataset con información visual (fotos, IDs)).

Scripts adicionales
- scrapping.py (Script en Python para obtener imágenes de los jugadores).

## Requisitos

- R ≥ 4.2.0
- Power BI Desktop para visualizar los archivos .pbix

- Paquetes necesarios en R
Este proyecto requiere los siguientes paquetes para su ejecución:

```r
install.packages(c(
  "dplyr", "tidyverse", "ggplot2", "cluster", "factoextra",
  "fastDummies", "psych", "fmsb", "corrplot", "broom",
  "sigr", "lubridate", "arules", "dendextend", "purrr",
  "readxl", "writexl", "plotly", "knitr", "rmarkdown"
))
```

## Cómo ejecutar: 

1. Abre Proyecto Unsupervised Learning (NBA) - DMyML.Rmd en RStudio.
2. Asegúrate de tener los archivos .csv y .xlsx en el mismo directorio.
3. Ejecuta todo el script (Knit) para generar el reporte HTML.
4. Abre el archivo .pbix en Power BI para explorar el dashboard interactivo.
5. Consulta el archivo PDF de presentación para una vista resumida y comentada de los hallazgos.

## Desarrolladores: 
Marco Carbajal (marcocarbajalb)
Diego Monroy
Carlos Aldana (C3AC)
Carlos Angel (CarFAngM)
José Donado (donaditoUVG)

