# Diseño del programa

## Objetivo

Analizar resultados de expresión diferencial obtenidos con DESeq2 para identificar genes significativamente regulados durante infección por Influenza A Virus.

### Entrada
Se usará una lista para almacenar los genes válidos leídos. Cada gen se representará como una tupla:
(gene, log2FoldChange, padj)

### Salida
Se usará una lista para almacenar los genes significativos filtrados. Cada gen se representará como una tupla extendida con su estado:
(gene, log2FoldChange, padj, status)

Donde 'status' puede ser:
- upregulated
- downregulated

## Algoritmo

1. Leer archivo TSV.
2. Extraer gene, log2FoldChange y padj.
3. Revisar cada gen.
4. Aplicar criterios de significancia:
   - padj < 0.05
   - abs(log2FoldChange) >= 1
5. Clasificar:
   - upregulated
   - downregulated
6. Guardar resultados.
7. Mostrar resumen.

## Estructuras de datos

### Entrada

Lista de diccionarios:

```python
[
    {
        "gene": "IFIT1",
        "log2FoldChange": 2.3,
        "padj": 0.001
    }
]
```

### Salida

Lista de diccionarios:

```python
[
    {
        "gene": "IFIT1",
        "log2FoldChange": 2.3,
        "padj": 0.001,
        "classification": "upregulated"
    }
]
```

## Funciones sugeridas

1. load_deseq2_results(filename): Lee el archivo de entrada e ignora líneas inválidas, regresando una lista de tuplas de genes válidos.
2. is_significant(log2_fold_change, padj, lfc_threshold, padj_threshold): Evalúa si un gen cumple los criterios de significancia.
3. classify_gene(log2_fold_change): Clasifica el gen como 'upregulated' o 'downregulated'.
4. filter_genes(results, lfc_threshold, padj_threshold): Recorre la lista de genes válidos, aplica la significancia y los clasifica.
5. write_results(output_file, filtered_genes): Guarda los resultados filtrados en el archivo de salida con el encabezado correspondiente.
6. print_summary(filtered_genes): Muestra el resumen estadístico final en pantalla.
7. main(): Coordina el flujo general y maneja los argumentos de la línea de comandos.

## Diagrama de flujo

```mermaid
flowchart TD

A[Inicio] --> B[Leer TSV]
B --> C[Procesar gen]

C --> D{padj < 0.05 y abs(log2FC) >= 1?}

D -->|No| E[Siguiente gen]
D -->|Sí| F[Clasificar gen]

F --> G[Guardar resultado]
G --> E

E --> H{Quedan genes?}

H -->|Sí| C
H -->|No| I[Escribir TSV]

I --> J[Mostrar resumen]
J --> K[Fin]
```
