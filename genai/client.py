import requests

BASE_URL = "http://127.0.0.1:8000"

def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    payload = {"name": name, "category": category}
    try:
        res = requests.post(f"{BASE_URL}/products", json=payload)
        res.raise_for_status()
        print("\n✅ Product added!")
        print(res.json())
    except requests.exceptions.RequestException as e:
        print("❌ Error adding product:", e)

def list_products():
    try:
        res = requests.get(f"{BASE_URL}/products")
        res.raise_for_status()
        products = res.json()
        if products:
            print("\n📦 Product list:")
            for p in products:
                print(f"- {p['name']} ({p['category']}): {p['description']}")
        else:
            print("\n🔍 No products in the database.")
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching products:", e)

def filter_by_category():
    category = input("Enter category: ")
    try:
        res = requests.get(f"{BASE_URL}/products/{category}")
        res.raise_for_status()
        products = res.json()
        print(f"\n🔎 Products in category '{category}':")
        for p in products:
            print(f"- {p['name']} ({p['category']}): {p['description']}")
    except requests.exceptions.HTTPError as e:
        if res.status_code == 404:
            print("⚠️ No products found in this category.")
        else:
            print("❌ Error:", e)
    except requests.exceptions.RequestException as e:
        print("❌ Error searching:", e)

def main():
    while True:
        print("\n📘 MENU:")
        print("1. Add product")
        print("2. View all products")
        print("3. Filter products by category")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            filter_by_category()
        elif choice == "0":
            print("👋 Exiting.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
