import os
if os.name == 'nt':
    import msvcrt

print("Zar oyununa hoþ geldiniz!")
if os.name == 'nt':
    msvcrt.getch()
else:
    input("Devam etmek için Enter tuþuna basýn...")


zar = random.randint(1, 6)
print("Zarýn attýðý sayý:", zar)

if zar == 1:
    print("Kaybettiniz!")
elif zar == 6:
    print("Tebrikler, kazandýnýz!")
else:
    print("Tekrar deneyin!")