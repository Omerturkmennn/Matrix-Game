
import numpy as np
import random

def olustur_matris(satir, sutun, alt=2, ust=35):
    return np.random.randint(alt, ust+1, size=(satir, sutun))

def zar_ati():
    return random.randint(1,6), random.randint(1,6), random.randint(1,6)

def ortanca_zar(zarlar):
    en_buyuk = max(zarlar)
    en_kucuk = min(zarlar)
    return sum(zarlar) - (en_buyuk + en_kucuk), en_buyuk, en_kucuk

def main():
    satir = int(input("Matrisin kaç satırdan oluşmasını istersiniz: "))
    sutun = int(input("Matrisin kaç sütundan oluşmasını istersiniz: "))

    M = olustur_matris(satir, sutun)
    print("Oluşturulan Matris:")
    print(M)

    while True:
        zar1, zar2, zar3 = zar_ati()
        print(f"\nZarlar: {zar1}, {zar2}, {zar3}")
        ortanca, en_buyuk, en_kucuk = ortanca_zar([zar1, zar2, zar3])
        sonuc = ortanca * en_buyuk + en_kucuk
        print(f"Matris içinde aranacak değer: {sonuc}")

        bulundu = False
        for i in range(satir):
            for j in range(sutun):
                if M[i,j] == sonuc:
                    M[i,j] = -1
                    print(f"Matrisin {i+1}. satırının {j+1}. sütunu -1 yapıldı")
                    bulundu = True
                    break
            if bulundu:
                break

        if not bulundu:
            print(f"Matris içerisinde {sonuc} değeri bulunamadı")

        print("Güncellenen Matris:")
        print(M)

        # Satır tamamen -1 olduysa dur
        for i in range(satir):
            if all(M[i,:] == -1):
                print(f"Matrisin {i+1}. satırının tüm elemanları -1 olduğu için program sonlandırıldı")
                return

if __name__ == "__main__":
    main()
