# Membuat class Cat dengan method say
# Kita mengubah penamaan parameter "self" dengan nama "myParam"
class Cat:
    color = "black"

    def say(myParam):
        print("My color is %s" % myParam.color)


# Membuat objek baru
cat1 = Cat()
# Memanggil method di dalam Class
cat1.say()
