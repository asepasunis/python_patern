command = input("masukan perintah:(hello, [hello, asep], [jumlahkan, angka]): ")
inputs = command.split(' ')

match inputs:

    case ["hello"]:
        name = input("nama anda: ")
        print("hello ", name)

    case ["hello", "asep"]:
        print("hello asep, apa kabar?")

    case ["jumlahkan","angka"]:
        numbers = input("masukan urutan angka integer, pisahkan dengan spasi :")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)
    case ["jumlahkan","angka", *args]:
        total = 0
        for str in args:
            total = total + int(str)
        print("total:", total)
    case _:
        print("perintah tidak diketahui:")