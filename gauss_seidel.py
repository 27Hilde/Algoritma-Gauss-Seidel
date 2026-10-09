
import numpy as np

# Matriks koefisien SPL
A = np.array([
    [10, -1,  2],
    [-1, 11, -1],
    [2, -1, 10]
], dtype=float)

# Konstanta persamaan
b = np.array([6, 22, -10], dtype=float)

# Nilai awal variabel
x = np.array([0.0, 0.0, 0.0])

# Toleransi dan iterasi maksimum
toleransi = 0.0001
maks_iterasi = 100

# Memeriksa elemen diagonal
if np.any(np.diag(A) == 0):
    raise ValueError("Elemen diagonal tidak boleh nol.")

# Proses iterasi Gauss-Seidel
print("HASIL ITERASI METODE GAUSS-SEIDEL")
print("-" * 60)

konvergen = False

for iterasi in range(1, maks_iterasi + 1):
    x_lama = x.copy()

    for i in range(len(b)):
        jumlah = 0.0

        for j in range(len(b)):
            if j != i:
                jumlah += A[i, j] * x[j]

        x[i] = (b[i] - jumlah) / A[i, i]

    error = np.max(np.abs(x - x_lama))

    print(
        f"Iterasi {iterasi}: "
        f"x1 = {x[0]:.6f}, "
        f"x2 = {x[1]:.6f}, "
        f"x3 = {x[2]:.6f}, "
        f"Error = {error:.8f}"
    )

    if error <= toleransi:
        konvergen = True
        break

# Menampilkan hasil akhir
print("\nHASIL AKHIR")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.6f}")

print(f"Jumlah iterasi = {iterasi}")
print(f"Error terakhir = {error:.8f}")

if konvergen:
    print("Status: Konvergen")
else:
    print("Status: Belum konvergen")
