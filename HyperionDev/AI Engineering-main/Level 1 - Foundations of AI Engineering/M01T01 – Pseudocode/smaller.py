import pikepdf

def compress_pdf(input_path, output_path):
    with pikepdf.open(input_path) as pdf:
        # Optional: clear metadata
        pdf.docinfo.clear()

        # Optional: remove unreferenced embedded resources
        pdf.remove_unreferenced_resources()

        # Save with compression (default behavior is sufficient)
        pdf.save(output_path, linearize=True)

# Example usage
compress_pdf("03-003_Pseudocode.pdf", "output_compressed.pdf")
