# string’te f kullanımı
ad = input('Adın ne?')
print ("Demek adın ", ad)

# yil = input("Hangi yılda doğdun",ad) hata verir
yil = input(f"Hangi yılda doğdun {ad}?")
print(f"yanı {2025-int(yil)} yaşındasın {ad}.")
