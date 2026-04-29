print("=== HESAP MAKİNESİNE HOŞ GELDİNİZ ===")

gecmis = []
islem_sayisi = 0

def hesapla_ifade(ifade):
    try:
        if "+" in ifade:
            a, b = ifade.split("+")
            return float(a) + float(b), "+"
        elif "-" in ifade:
            a, b = ifade.split("-")
            return float(a) - float(b), "-"
        elif "*" in ifade:
            a, b = ifade.split("*")
            return float(a) * float(b), "*"
        elif "/" in ifade:
            a, b = ifade.split("/")
            if float(b) == 0:
                return "HATA", "/"
            return float(a) / float(b), "/"
        else:
            return None, None
    except:
        return None, None

while True:

    print("""
1- Toplama (+)
2- Çıkarma (-)
3- Çarpma (*)
4- Bölme (/)
5- Tek satır işlem (örn: 5+3)
h- Geçmiş
q- Çıkış
""")

    secim = input("Seçiminizi yapınız: ")

    if secim == "q":
        print("Programdan çıkılıyor...")
        break

    if secim == "h":
        print("\n--- GEÇMİŞ ---")
        if not gecmis:
            print("Henüz işlem yok")
        else:
            for i in gecmis:
                print(i)
        continue

    # 🔥 TEK SATIR İŞLEM
    if secim == "5":
        ifade = input("İşlemi giriniz (örn: 5+3): ")
        sonuc, operator = hesapla_ifade(ifade)

        if sonuc == "HATA":
            print("❌ 0'a bölünemez")
            continue

        if sonuc is None:
            print("❌ Geçersiz ifade")
            continue

        print("Sonuç:", sonuc)
        gecmis.append(f"{ifade} = {sonuc}")
        islem_sayisi += 1
        continue

    if secim not in ["+", "-", "*", "/"]:
        print("❌ Geçersiz seçim")
        continue

    try:
        ilksayi = float(input("Birinci sayıyı giriniz: "))
        ikincisayi = float(input("İkinci sayıyı giriniz: "))
    except:
        print("❌ Hatalı sayı girdiniz")
        continue

    if secim == "+":
        sonuc = ilksayi + ikincisayi

    elif secim == "-":
        sonuc = ilksayi - ikincisayi

    elif secim == "*":
        sonuc = ilksayi * ikincisayi

    elif secim == "/":
        if ikincisayi == 0:
            print("❌ 0'a bölünemez")
            continue
        sonuc = ilksayi / ikincisayi

    print("Sonuç:", sonuc)
    gecmis.append(f"{ilksayi} {secim} {ikincisayi} = {sonuc}")
    islem_sayisi += 1


# 💾 DOSYAYA KAYDETME
with open("gecmis.txt", "w") as f:
    for i in gecmis:
        f.write(i + "\n")

# 📊 SON BİLGİLER
print("\n--- SON GEÇMİŞ ---")
for i in gecmis:
    print(i)

print("Toplam işlem sayısı:", islem_sayisi)
print("Program kapandı")