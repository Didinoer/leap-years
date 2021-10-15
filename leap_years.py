print("cek tahun kabisat atau bukan")


while True : 
    tahun = int(input('masukan tahun berapa sekarang : '))


    if tahun%4 == 0 :
        if tahun%100 == 0 :
            if tahun%400 == 0 :
                print("ini tahun kabisat ")
            else:
                print("ini bukan tahun kabisat")
        else : 
            print (" ini tahun kabisat")
    else:
        print("ini bukan tahun kabisat")
