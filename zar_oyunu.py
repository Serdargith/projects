import os
if os.name == 'nt':
    import msvcrt

print("Zar oyununa ho� geldiniz!")
if os.name == 'nt':
    msvcrt.getch()
else:
    input("Devam etmek i�in Enter tu�una bas�n...")


zar = random.randint(1, 6)
print("Zar�n att��� say�:", zar)

if zar == 1:
    print("Kaybettiniz!")
elif zar == 6:
    print("Tebrikler, kazand�n�z!")
else:
    print("Tekrar deneyin!")