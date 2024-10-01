command = input("masukan perintah: ")

if command == "hello":
    name = input("nama anda: ")
    print("hello", name)

elif command == "jumlahkan angka":
    numbers = input("masukan urutan angka integer, pisahkan dengan spasi :")
    total = 0
    for str in numbers.split(' '):
        total = total + int(str)
    print("total:", total)

elif command == "acak angka":
    import random
    n = random.randint(0, 100)
    print("angka acak:", n)

else:
    print("perintah tidak dikenali")