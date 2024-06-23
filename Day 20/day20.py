# Fungsi untuk mengurutkan daftar menggunakan algoritma pengurutan gelembung (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Fungsi untuk melakukan pencarian biner
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Contoh Penggunaan
# Daftar angka
numbers = [64, 34, 25, 12, 22, 11, 90]

# Mengurutkan daftar angka
sorted_numbers = bubble_sort(numbers.copy())
print("Sorted List:", sorted_numbers)

# Angka yang akan dicari
target = 25

# Melakukan pencarian biner
result = binary_search(sorted_numbers, target)

# Menampilkan hasil pencarian
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in the list")
