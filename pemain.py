import os
#Tugas Praktikum Konsep Teknologi
#author: Anastasyarez

#input pemain
def entry():
    lagi = "y"
    while (lagi=="y"):
        print("")

        nama = input("Nama Pemain: ")
        posisi = input("Posisi : ")

        f = open("pemain.txt", "a")
        f.write(nama + "\t\t" + posisi+"\n")

        lagi = input("Isi lagi? (y/t): ")
    f.close()
    print("--------------------------")
    print("Terima kasih sudah mengisi! \n")

def view():
    f = open("pemain.txt", "r")
    text = f.readline()
    no = 1
    print("--------------------------")
    print("VIEW\nNo\tNama Pemain\t\tPosisi")
    while (text):
        print(str(no) +" \t\t" + text.strip())
        text = f.readline()
        no+=1
    f.close()
    print("----------------------------------------------------------")
    os.system("PAUSE")
    print("Terima kasih~\n")

pilih = ''
while (pilih != 'X'):
    try:
        print("====PROGRAM ENTRY PEMAIN====")
        print("(E). ENTRY\n(V). VIEW \n(X). EXIT")
        pilih = input("Pilih Menu: ")

        if pilih == 'E':
            entry()
        elif pilih == 'V':
            view()
        elif pilih == 'X':
            print("C U SOON!")

    except ValueError:
        print("\nInput dengan benar!\n")
