# Casos de prueba

Para validar el correcto funcionamiento del programa `analyze_iav.py`, se definen los siguientes 7 casos de prueba mínimos que cubren escenarios biológicos y de robustez del código.

## Tabla de Casos de Prueba (Datos de Entrada y Salida Esperada)

| ID | Tipo de Caso | Gen | log2FoldChange | padj | Comportamiento / Salida Esperada | Tipo de Validación |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Sobreexpresado | `IFIT1` | `2.5` | `0.001` | Incluido en la salida con status `upregulated` | Lógica biológica |
| **2** | Subexpresado | `CXCL10` | `-2.2` | `0.003` | Incluido en la salida con status `downregulated` | Lógica biológica |
| **3** | No sig. por `padj` | `STAT1` | `3.0` | `0.10` | Filtrado (No debe aparecer en el archivo de salida) | Lógica biológica |
| **4** | No sig. por `log2FC` | `IRF7` | `0.5` | `0.001` | Filtrado (No debe aparecer en el archivo de salida) | Lógica biológica |
| **5** | Valor ausente (`NA`) | `IFITM3` | `NA` | `0.001` | Línea ignorada de forma segura sin detener el programa | Robustez (Errores de tipo) |
| **6** | Línea incompleta | `MX1` | `1.8` | *Faltante* | Línea ignorada de forma segura por falta de columnas | Robustez (Formato de archivo) |

---

## Casos de Error del Sistema

### Caso 7: Archivo de entrada no existente
* **Condición de entrada:** Ejecutar el programa pasando una ruta de archivo que no existe en el disco, por ejemplo:
  ```bash
  python analyze_iav.py data/archivo_fantasma.tsv results/salida.tsv