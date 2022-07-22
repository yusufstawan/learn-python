# Membuat lists yang berisi nama-nama hewan
animals = ["Ayam", "Bebek", "Cicak"]

# Kita bisa mengakses item di dalam "Lists" berdasarkan urutannya (indexing)
# semisal kita ingin mengakses item "Bebek" (urutan kedua), maka kita bisa menggunakan indexing "1"
# kenapa tidak menggunakan indexing "2"? karena indexing dimulai dari angka 0, bukan 1 (n - 1)

print(animals[1])  # Bebek

# Jika kita ingin mengakses dengan urutan sebaliknya (dari urutan paling akhir),
# kita bisa menggunakan negative indexing
# Jika kita menggunakan indexing "-1", artinya kita mengakses item terakhir
# Jika menggunakan indexing "-2", artinya kita mengakses item kedua dari urutan terakhir

print(animals[-1])  # Cicak
print(animals[-2])  # Bebek
