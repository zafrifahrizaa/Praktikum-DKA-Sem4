import numpy as np   
n = int(input("Masukkan jumlah mahasiswa: "))

nama = []      # string
nim = []       # string
nilai = []     # float
tahun = []     # integer

for i in range(n):
    print("\nData Mahasiswa ke-", i+1)
    
    nama.append(input("Nama        : "))            
    nim.append(input("NIM         : "))             
    nilai.append(float(input("Nilai       : ")))    
    tahun.append(int(input("Tahun Masuk : ")))      

# ubah list menjadi array numpy
nama = np.array(nama)     
nim = np.array(nim)       
nilai = np.array(nilai)   
tahun = np.array(tahun)  

# menampilkan seluruh data mahasiswa
for i in range(n):
    print("Nama :", nama[i])           
    print("NIM  :", nim[i])            
    print("Nilai:", nilai[i])          
    print("Tahun Masuk:", tahun[i])    
    print("----------------------")

# menghitung nilai menggunakan numpy
print("Nilai Tertinggi :", np.max(nilai))   
print("Nilai Terendah  :", np.min(nilai))   
print("Nilai Rata-rata :", np.mean(nilai))  

# meminta input untuk pencarian data mahasiswa
cari = input("\nMasukkan Nama atau NIM yang ingin dicari: ")  

for i in range(n):
    if cari == nama[i] or cari == nim[i]:   
        print("\nData Mahasiswa Ditemukan")
        print("Nama :", nama[i])
        print("NIM  :", nim[i])
        print("Nilai:", nilai[i])
        print("Tahun Masuk:", tahun[i])
