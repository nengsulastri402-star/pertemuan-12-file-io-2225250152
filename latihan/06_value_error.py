# Latihan 6: Penanganan ValueError
teks = input("Masukkan nilai numerik: ")
try:
    nilai = float(teks)
    print(f"Nilai valid: {nilai}")
except ValueError:
    print("Pesan Error: Input harus berupa angka valid.")
