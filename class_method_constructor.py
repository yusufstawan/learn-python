# Membuat Class Cat dengan property color dan menambahkan method constructor
# Kita akan menambahkan method constructor untuk mengubah nilai dari properti color
class Cat:
    color = "black"

    def __init__(self, color):
        self.color = color


# Membuat objek baru
cat1 = Cat("orange")
print(cat1.color)  # orange
