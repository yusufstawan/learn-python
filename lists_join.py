# Menggabungkan sebuah "Lists" dengan "Lists" lainnya
animals = ["Ayam", "Bebek", "Cicak"]
otherAnimals = ["Domba", "Elang", "Gajah"]
animals.extend(otherAnimals)
print(animals)  # ["Ayam", "Bebek", "Cicak", "Domba", "Elang", "Gajah"]

fruits = ["Apel", "Mangga", "Pisang"]
otherFruits = ["Durian", "Semangka", "Jeruk"]
allFruits = fruits + otherFruits
print(allFruits)  # ["Apel", "Mangga", "Pisang", "Durian", "Semangka", "Jeruk"]
