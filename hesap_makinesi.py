print("=== HESAP MAKİNESİNE HOŞ GELDİNİZ ===")

gecmis = []
islem_sayisi = 0

def hesapla_ifade(ifade):
    try:
        # Boşlukları temizleyelim (örn: "5 + 3" -> "5+3")
        ifade = ifade.replace(" ", "")
        
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
    except ValueError:
        return None, None
    except ZeroDivisionError:
        return "HATA", "/"
    except Exception:
        return None, None

while True:
    print("""
========== MENÜ ==========
1- Toplama (+)
2- Çıkarma (-)
3- Çarpma (*)
4- Bölme (/)
5- Tek satır işlem (örn: 5+3)
h- Geçmişi Görüntüle
q- Programdan Çık
==========================""")

    secim = input("Seçiminizi yapınız: ").lower()

    if secim == "q":
        print(f"Programdan çıkılıyor... Toplam {islem_sayisi} işlem yapıldı.")
        break

    if secim == "h":
        print("\n--- GEÇMİŞ ---")
        if not gecmis:
            print("Henüz işlem yok.")
        else:
            for i in gecmis:
                print(i)
        continue

    sonuc = None
    islem_metni = ""

    # SEÇENEK 5: TEK SATIR İŞLEM
    if secim == "5":
        ifade = input("İşlemi giriniz (örn: 5+3): ")
        sonuc, operator = hesapla_ifade(ifade)

        if sonuc == "HATA":
            print("❌ Hata: Sıfıra bölünemez!")
            continue
        if sonuc is None:
            print("❌ Hata: Geçersiz ifade!")
            continue
        islem_metni = f"{ifade} = {sonuc}"

    # SEÇENEK 1-4: STANDART İŞLEMLER
    elif secim in ["1", "2", "3", "4", "+", "-", "*", "/"]:
        try:
            ilksayi = float(input("Birinci sayıyı giriniz: "))
            ikincisayi = float(input("İkinci sayıyı giriniz: "))
            
            if secim in ["1", "+"]:
                sonuc = ilksayi + ikincisayi
                op = "+"
            elif secim in ["2", "-"]:
                sonuc = ilksayi - ikincisayi
                op = "-"
            elif secim in ["3", "*"]:
                sonuc = ilksayi * ikincisayi
                op = "*"
            elif secim in ["4", "/"]:
                if ikincisayi == 0:
                    print("❌ Hata: Sıfıra bölünemez!")
                    continue
                sonuc = ilksayi / ikincisayi
                op = "/"
            islem_metni = f"{ilksayi} {op} {ikincisayi} = {sonuc}"
        except ValueError:
            print("❌ Hata: Lütfen sadece sayısal değerler giriniz!")
            continue
    else:
        print("❌ Hata: Geçersiz bir seçim yaptınız!")
        continue

    # SONUÇ GÖSTERİMİ VE KAYIT (Sadece başarılı işlemlerde çalışır)
    if sonuc is not None:
        print(f"\n>>> Sonuç: {sonuc}")
        gecmis.append(islem_metni)
        islem_sayisi += 1
        
        # Veri kalıcılığı için anlık dosya kaydı
        with open("gecmis.txt", "a", encoding="utf-8") as f:
            f.write(islem_metni + "\n")

print("Program kapandı.")