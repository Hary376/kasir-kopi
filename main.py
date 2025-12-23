# Inisialisasi data toko
toko = "KOPI-KOPI LITE"
menu_kopi = {
    "Kopi Hitam": {"harga": 10000, "stok": 5},
    "Kopi Susu": {"harga": 15000, "stok": 10},
    "Matcha Latte": {"harga": 20000, "stok": 3}
}

print(f"=== SELAMAT DATANG DI {toko} ===")

while True:
    # 1. Tampilkan Menu
    print("\nDAFTAR MENU & STOK:")
    for produk, info in menu_kopi.items():
        print(f"- {produk:15} | Harga: Rp{info['harga']:,} | Stok: {info['stok']}")
    
    # 2. Input Pesanan
    pesanan = input("\nKetik nama menu yang ingin dibeli (atau 'keluar' untuk tutup): ").title()

    if pesanan == "Keluar":
        print("Terima kasih telah berkunjung!")
        break

    if pesanan in menu_kopi:
        try:
            jumlah = int(input(f"Mau beli berapa {pesanan}? "))
            
            # 3. Validasi Stok
            stok_tersedia = menu_kopi[pesanan]["stok"]
            
            if jumlah <= stok_tersedia:
                total_harga = jumlah * menu_kopi[pesanan]["harga"]
                
                # Update Stok
                menu_kopi[pesanan]["stok"] -= jumlah
                
                print(f"\n--- STRUK PEMBAYARAN ---")
                print(f"Item  : {pesanan} x {jumlah}")
                print(f"Total : Rp{total_harga:,}")
                print(f"------------------------")
                print(f"Sisa stok {pesanan} sekarang: {menu_kopi[pesanan]['stok']}")
            else:
                print(f"❌ Maaf, stok tidak cukup. (Tersedia: {stok_tersedia})")
                
        except ValueError:
            print("❌ Masukkan angka yang valid untuk jumlah beli!")
    else:
        print("❌ Menu tidak tersedia. Silakan pilih menu yang ada di daftar.")
