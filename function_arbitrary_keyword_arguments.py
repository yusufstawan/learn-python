def belajar_python(**student):
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))


# Memanggil Function belajar_python dengan Arbitrary Keyword Arguments
belajar_python(age=20, name="Rizqi")  # Halo, Saya Rizqi. Umur Saya 30
