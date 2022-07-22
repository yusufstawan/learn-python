animals = ["Ayam", "Bebek", "Cicak"]

# Menghapus item tertentu (Bebek) pada "Lists" dengan method "remove"
animals.remove("Bebek")
print(animals)  # ["Ayam", "Cicak"]

# Menghapus item terakhir pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals)  # ["Ayam", "Bebek"]

# Menghapus item berdasarkan posisinya (indexing) pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals)  # ["Bebek", "Cicak"]

# Menghapus semua item pada "Lists" dengan method "clear"
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals)  # []
