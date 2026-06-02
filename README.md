# Analizador de Expresión Diferencial (DESeq2 - IAV)

Este proyecto contiene un script en Python diseñado para procesar, filtrar y clasificar datos de expresión diferencial de genes provenientes de análisis de RNA-Seq con DESeq2, específicamente enfocados en la infección por el Virus de la Influenza A (IAV).

## Estructura del Proyecto

- `data/`: Contiene los archivos de datos de entrada (TSV).
- `docs/`: Documentación del diseño del software y casos de prueba.
- `results/`: Archivos de salida con los genes significativos identificados.
- `analyze_iav.py`: Script principal de procesamiento.

## Requisitos y Ejecución

El proyecto utiliza `argparse` para permitir una ejecución dinámica desde la línea de comandos y está gestionado con el entorno `uv`.

### Ejecución básica (Umbrales por defecto: LFC >= 1.0, padj < 0.05)
```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv