print("+ YAPILACAKLAR LİSTESİ +")
yapilacaklar = []
while True:
  print("1. Yapılacak ekle")
  print("2. Yapılacakları göster")
  print("3. Yapılacakları sil")
  print("4. Çıkış")
  secim = input ("Yapmak istediğiniz işlemin numarasını girin: ")


  if secim == "1":
    yeni_is = input("Yapılacak işi girin: ")
    yapilacaklar.append(yeni_is)
    print ("Yapılacak iş eklendi. ")

  elif secim == "2":
    print("\n--- Yapılacaklar Listesi--- :")
    if len(yapilacaklar) == 0:
      print("Liste şuan bomboş kanki. ")
    else: 
       sayac = 1
       for gorev in yapilacaklar :
        print(str(sayac) + ". " + (gorev))
        sayac = sayac + 1



    

  