"""
Tugas 5: Rekap Nilai dari File
Nama    : [Nama Anda]
NIM     : [NIM Anda]
Kelas   : [Kelas Anda]
"""

def baca_data(nama_file):
    """
    Membaca data dari file input, memvalidasi setiap baris,
    dan mengembalikan list of tuple berisi (NIM, nilai).
    """
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                # Abaikan baris kosong
                if not baris:
                    continue
                
                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai.strip())
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"[Peringatan] Baris {nomor} dilewati (format/nilai tidak valid): '{baris}'")
                except IndexError:
                    print(f"[Peringatan] Baris {nomor} dilewati (sintaks split tidak sesuai): '{baris}'")
                    
    except FileNotFoundError:
        print(f"[Error] File input '{nama_file}' tidak ditemukan.")
        return None
        
    return data


def tulis_rekap(nama_file, data):
    """
    Menghitung statistik dasar dari data valid dan menuliskan 
    ringkasan ke file output.
    """
    if not data:
        print("[Info] Tidak ada data valid untuk direkap.")
        return False

    nilai_list = [item[1] for item in data]
    jumlah_data = len(nilai_list)
    rata_rata = sum(nilai_list) / jumlah_data
    nilai_min = min(nilai_list)
    nilai_max = max(nilai_list)
    jumlah_lulus = sum(1 for x in nilai_list if x >= 60)

    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write("==============================\n")
            file.write("      HASIL REKAP NILAI       \n")
            file.write("==============================\n")
            file.write(f"Jumlah data valid : {jumlah_data}\n")
            file.write(f"Rata-rata nilai   : {rata_rata:.2f}\n")
            file.write(f"Nilai Minimum     : {nilai_min:.2f}\n")
            file.write(f"Nilai Maksimum    : {nilai_max:.2f}\n")
            file.write(f"Jumlah Lulus (>=60): {jumlah_lulus}\n")
            file.write("==============================\n")
        
        print(f"[Sukses] Hasil rekapitulasi berhasil ditulis ke '{nama_file}'.")
        return True
    except Exception as e:
        print(f"[Error] Gagal menulis ke file output: {e}")
        return False


def main():
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"

    print("--- Memulai Proses Rekapitulasi Data ---")
    data_valid = baca_data(input_file)

    if data_valid is not None:
        print(f"[Info] Berhasil membaca {len(data_valid)} record valid.")
        tulis_rekap(output_file, data_valid)
    
    print("--- Proses Selesai ---")

if __name__ == "__main__":
    main()
