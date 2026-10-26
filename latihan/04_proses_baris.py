# Latihan 4: Memproses Baris Data (strip, split, konversi)
with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        nim, teks_nilai = baris.split(",")
        try:
            print(f"NIM: {nim}, Nilai: {float(teks_nilai)}")
        except ValueError:
            print(f"Format nilai tidak valid pada NIM {nim}: {teks_nilai}")