import requests

BASE_URL = "http://127.0.0.1:8000"

def add_product():
    name = input("Podaj nazwę produktu: ")
    category = input("Podaj kategorię produktu: ")
    payload = {"name": name, "category": category}
    try:
        res = requests.post(f"{BASE_URL}/products", json=payload)
        res.raise_for_status()
        print("\n✅ Produkt dodany!")
        print(res.json())
    except requests.exceptions.RequestException as e:
        print("❌ Błąd przy dodawaniu produktu:", e)

def list_products():
    try:
        res = requests.get(f"{BASE_URL}/products")
        res.raise_for_status()
        products = res.json()
        if products:
            print("\n📦 Lista produktów:")
            for p in products:
                print(f"- {p['name']} ({p['category']}): {p['description']}")
        else:
            print("\n🔍 Brak produktów w bazie.")
    except requests.exceptions.RequestException as e:
        print("❌ Błąd przy pobieraniu produktów:", e)

def filter_by_category():
    category = input("Podaj kategorię: ")
    try:
        res = requests.get(f"{BASE_URL}/products/{category}")
        res.raise_for_status()
        products = res.json()
        print(f"\n🔎 Produkty w kategorii '{category}':")
        for p in products:
            print(f"- {p['name']} ({p['category']}): {p['description']}")
    except requests.exceptions.HTTPError as e:
        if res.status_code == 404:
            print("⚠️ Nie znaleziono produktów w tej kategorii.")
        else:
            print("❌ Błąd:", e)
    except requests.exceptions.RequestException as e:
        print("❌ Błąd przy wyszukiwaniu:", e)

def main():
    while True:
        print("\n📘 MENU:")
        print("1. Dodaj produkt")
        print("2. Wyświetl wszystkie produkty")
        print("3. Filtruj produkty po kategorii")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            filter_by_category()
        elif choice == "0":
            print("👋 Zakończono.")
            break
        else:
            print("❌ Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
