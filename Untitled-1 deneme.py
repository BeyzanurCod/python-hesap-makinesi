print("🧮 CALC BAŞLADI")

history = []

while True:
    expr = input("İşlem gir: ")

    if expr == "q":
        break

    if expr == "h":
        print("\n--- GEÇMİŞ ---")
        for h in history:
            print(h)
        print("--------------\n")
        continue

    try:
        result = eval(expr)
        history.append(f"{expr} = {result}")
        print("Sonuç:", result)

    except Exception:
        print("❌ Geçersiz işlem!")
        