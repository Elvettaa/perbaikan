# Masukkan nilai n
n = int(input("Masukkan nilai n: "))
# Tetapkan nilai awal total dan i
total = 0
i = 1
# Loop untuk menghitung jumlah bilangan dari 1 hingga n
while i <= n:
    total += i  # Tambahkan i ke total
    i += 1      # Tingkatkan i sebesar 1
# Tampilkan hasil
print("Jumlah bilangan dari 1 hingga", n, "adalah:", total)
