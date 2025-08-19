import os

os.makedirs("results", exist_ok=True)

# Amino acid weights (average)
aa_weights = {
    'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15,
    'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.17,
    'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
    'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
}

# Load protein sequence
with open("data/protein.txt") as f:
    protein = f.read().strip().upper()

weight = sum([aa_weights.get(aa, 0) for aa in protein])
aa_count = {aa: protein.count(aa) for aa in aa_weights.keys()}

# Save results
with open("results/protein_results.txt", "w") as f:
    f.write(f"Protein length: {len(protein)}\n")
    f.write(f"Molecular weight: {weight:.2f} Da\n")
    f.write("Amino acid composition:\n")
    for aa, count in aa_count.items():
        f.write(f"{aa}: {count}\n")

print("Protein analysis complete!")
