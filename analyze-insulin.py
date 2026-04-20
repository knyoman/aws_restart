# Masukkan 110 karakter bersih ke dalam variabel
preproinsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Melakukan slicing (pemotongan)
lsinsulin = preproinsulin[0:24]
binsulin = preproinsulin[24:54]
cinsulin = preproinsulin[54:89]
ainsulin = preproinsulin[89:110]

# Mencetak hasil untuk verifikasi
print(f"lsinsulin: {lsinsulin} (Length: {len(lsinsulin)})")
print(f"binsulin: {binsulin} (Length: {len(binsulin)})")
print(f"cinsulin: {cinsulin} (Length: {len(cinsulin)})")
print(f"ainsulin: {ainsulin} (Length: {len(ainsulin)})")

# Bagian ini akan menyimpan hasil ke file masing-masing otomatis
with open("lsinsulin-seq-clean.txt", "w") as f: f.write(lsinsulin)
with open("binsulin-seq-clean.txt", "w") as f: f.write(binsulin)
with open("cinsulin-seq-clean.txt", "w") as f: f.write(cinsulin)
with open("ainsulin-seq-clean.txt", "w") as f: f.write(ainsulin)