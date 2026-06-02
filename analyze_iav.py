import argparse


def load_deseq2_results(filename):
    """
    Lee resultados DESeq2 desde un archivo TSV.
    """

    genes = []

    with open(filename) as file:

        next(file)

        for line in file:

            line = line.strip()

            if not line:
                continue

            parts = line.split("\t")

            if len(parts) < 3:
                continue

            gene = parts[0]

            try:

                log2_fold_change = float(parts[1])
                padj = float(parts[2])

            except ValueError:
                continue

            genes.append((gene, log2_fold_change, padj))

    return genes


def is_significant(log2_fold_change, padj, lfc_threshold=1, padj_threshold=0.05):
    """
    Determina si un gen es significativo.
    """

    return abs(log2_fold_change) >= lfc_threshold and padj < padj_threshold


def classify_gene(log2_fold_change):
    """
    Clasifica un gen significativo.
    """

    if log2_fold_change > 0:
        return "upregulated"

    return "downregulated"


def filter_genes(results, lfc_threshold=1, padj_threshold=0.05):
    """
    Filtra y clasifica genes significativos.
    """

    filtered_genes = []

    for gene, log2_fold_change, padj in results:

        if is_significant(log2_fold_change, padj, lfc_threshold, padj_threshold):

            status = classify_gene(log2_fold_change)

            filtered_genes.append((gene, log2_fold_change, padj, status))

    return filtered_genes


def write_results(output_file, filtered_genes):
    """
    Guarda los genes significativos en un archivo TSV.
    """

    with open(output_file, "w") as file:

        file.write("gene\tlog2FoldChange\tpadj\tstatus\n")

        for gene, log2_fold_change, padj, status in filtered_genes:

            file.write(f"{gene}\t" f"{log2_fold_change}\t" f"{padj}\t" f"{status}\n")


def print_summary(filtered_genes):
    """
    Muestra un resumen de los resultados.
    """

    total = len(filtered_genes)

    upregulated = 0
    downregulated = 0

    for gene, log2_fold_change, padj, status in filtered_genes:

        if status == "upregulated":
            upregulated += 1

        elif status == "downregulated":
            downregulated += 1

    print("\nResumen del análisis")
    print("--------------------")
    print(f"Genes significativos: {total}")
    print(f"Upregulated: {upregulated}")
    print(f"Downregulated: {downregulated}")


def parse_arguments():
    """
    Lee argumentos desde la línea de comandos.
    """
    parser = argparse.ArgumentParser(
        description="Analizador de genes diferencialmente expresados"
    )
    # Obligatorios
    parser.add_argument("input_file", help="Archivo TSV de entrada")
    parser.add_argument("output_file", help="Archivo TSV de salida")

    # OPCIONALES (Para cumplir la extensión de la guía)
    parser.add_argument(
        "--lfc_threshold",
        type=float,
        default=1.0,
        help="Umbral para log2FoldChange (por defecto: 1.0)",
    )
    parser.add_argument(
        "--padj_threshold",
        type=float,
        default=0.05,
        help="Umbral para padj (por defecto: 0.05)",
    )

    return parser.parse_args()


def main():
    """
    Coordina todo el flujo del programa.
    """
    args = parse_arguments()

    try:
        genes = load_deseq2_results(args.input_file)
    except FileNotFoundError:
        print(f"Error: no existe el archivo '{args.input_file}'")
        return

    # PASAMOS LOS UMBRALES DINÁMICOS DESDE ARGS
    filtered_genes = filter_genes(
        genes, lfc_threshold=args.lfc_threshold, padj_threshold=args.padj_threshold
    )

    write_results(args.output_file, filtered_genes)
    print_summary(filtered_genes)


if __name__ == "__main__":
    main()
