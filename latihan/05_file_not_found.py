# Latihan 5: Penanganan FileNotFoundError
try:
    with open("data/tidak_ada.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Pesan Error: File 'data/tidak_ada.txt' tidak ditemukan.")
