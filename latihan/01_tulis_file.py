# Latihan 1: Menulis File dengan mode 'w'
with open("data/catatan.txt", "w", encoding="utf-8") as file:
    file.write("Algoritma dan Pemrograman\n")
    file.write("Pertemuan 12\n")

print("Latihan 1: File 'data/catatan.txt' berhasil ditulis.")
