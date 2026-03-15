import numpy as np   
n = int(input("Masukkan jumlah barang: "))   
namaBarang = []     
kodeBarang = []     
jumlah = []         
harga = []          

for i in range(n):
    print("\nData Barang ke-", i+1)

    namaBarang.append(input("Nama Barang  : "))      
    kodeBarang.append(input("Kode Barang  : "))      
    jumlah.append(int(input("Jumlah       : ")))     
    harga.append(float(input("Harga Unit   : ")))    

# ubah list menjadi array numpy
namaBarang = np.array(namaBarang)     
kodeBarang = np.array(kodeBarang)     
jumlah = np.array(jumlah)            
harga = np.array(harga)               

total = jumlah * harga    

print("\n===== DATA INVENTARIS =====")

for i in range(n):
    print("Nama Barang :", namaBarang[i])     
    print("Kode Barang :", kodeBarang[i])     
    print("Jumlah      :", jumlah[i])         
    print("Harga Unit  :", harga[i])          
    print("Total Nilai :", total[i])          
    print("-----------------------------")

# total seluruh inventaris gudang dgn menjumlah 
print("Total Nilai Seluruh Inventaris :", np.sum(total))   

cari = input("\nMasukkan Nama atau Kode Barang yang dicari: ")   

for i in range(n):
    if cari == namaBarang[i] or cari == kodeBarang[i]:   
        print("\nBarang Found")
        print("Nama Barang :", namaBarang[i])
        print("Kode Barang :", kodeBarang[i])
        print("Jumlah      :", jumlah[i])
        print("Harga Unit  :", harga[i])
        print("Total Nilai :", total[i])
