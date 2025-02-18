import requests
import json

API_BASE_URL = "http://127.0.0.1:8000"

def print_response(response):
    """Print response data in a formatted way."""
    if response.status_code in [200, 201]:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def tambahkan_data_item():
    """Send POST request to create a new item."""
    print("Enter item details:")
    brand = input("Brand: ")
    warna = input("Warna: ")
    tahun = input("Tahun: ")
    price = float(input("Price: "))
    payload = {
        "brand": brand,
        "warna": warna,
        "tahun": tahun,
        "price": price
    }
    response = requests.post(f"{API_BASE_URL}/items", json=payload)
    print_response(response)

def tampilkan_semua_items():
    """Send GET request to fetch all items."""
    response = requests.get(f"{API_BASE_URL}/items")
    print_response(response)

def tampilkan_item_berdasarkan_id():
    """Send GET request to fetch an item by ID."""
    item_id = input("Enter item ID: ")
    response = requests.get(f"{API_BASE_URL}/items/{item_id}")
    print_response(response)

def perbarui_item():
    """Send PUT request to update an item."""
    item_id = input("Enter item ID to update: ")
    print("Enter updated details:")
    brand = input("Brand: ")
    warna = input("Warna: ")
    tahun = input("Tahun: ")
    price = float(input("Price: "))
    payload = {
        "brand": brand,
        "warna": warna,
        "tahun": tahun,
        "price": price
    }
    response = requests.put(f"{API_BASE_URL}/items/{item_id}", json=payload)
    print_response(response)

def hapus_data_item():
    """Send DELETE request to delete an item."""
    item_id = input("Enter item ID to delete: ")
    response = requests.delete(f"{API_BASE_URL}/items/{item_id}")
    print_response(response)

def main():
    """Main menu for CRUD operations."""
    while True:
        print("\nMenu:")
        print("1. Tambahkan data item")
        print("2. Tampilkan semua items")
        print("3. Tampilkan item berdasarkan ID")
        print("4. Perbarui item")
        print("5. Hapus data item")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            tambahkan_data_item()  # Corrected function name
        elif choice == "2":
            tampilkan_semua_items()  # Corrected function name
        elif choice == "3":
            tampilkan_item_berdasarkan_id()  # Corrected function name
        elif choice == "4":
            perbarui_item()  # Corrected function name
        elif choice == "5":
            hapus_data_item()  # Corrected function name
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
