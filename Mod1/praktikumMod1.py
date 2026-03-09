#A
print ("informatika")
a = 2 + 2
b = 5 *2
c = 5 / 2
d = 5 // 2
print(a)
print(b)
print(c)
print(d)

#B
str = "Praktikum DKA"
print(str)

str1 = "Praktikum DKA"
str2 = "Informatika"
result= str1 + " " + str2
print(result)

str = "Praktikum DKA"
result = str * 3
print(result)

str = "    Praktikum, DKA! "
print(str.strip())

str = "Hello, World!" #mengganti bagian string
replaced = str.replace("World", "Dunia") # replace(old, new)
print(replaced)


#no 1
def isKabisat(tahun: int) -> bool:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))

hasil = isKabisat(tahun)

if hasil:
    print(tahun, "True")
else:
    print(tahun, "False")
