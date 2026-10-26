# Latihan 3: Menambahkan data dengan mode 'a'
with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Latihan append berhasil.\n")

print("Latihan 3: Data berhasil ditambahkan ke 'data/catatan.txt'.")
