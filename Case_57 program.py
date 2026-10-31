def main():
    item_count = int(input("Number of menu items: "))
    menu = {}
    for _ in range(item_count):
        name = input("Item name: ").strip().lower()
        price = float(input("Price: "))
        stock = int(input("Available quantity: "))
        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return
        menu[name] = {"price": price, "stock": stock}

    order_count = int(input("Number of order lines: "))
    sales = 0.0
    for i in range(order_count):
        name = input(f"Order {i + 1} item: ").strip().lower()
        quantity = int(input("Quantity: "))
        if name not in menu:
            print("Rejected: item not on menu.")
        elif quantity <= 0:
            print("Rejected: quantity must be positive.")
        elif quantity > menu[name]["stock"]:
            print(f"Rejected: only {menu[name]['stock']} available.")
        else:
            line_total = menu[name]["price"] * quantity
            menu[name]["stock"] -= quantity
            sales += line_total
            print(f"Accepted: {quantity} x {name} = Rs. {line_total:.2f}")

    print(f"\nTotal sales: Rs. {sales:.2f}")
    print("Remaining stock:")
    for name, details in menu.items():
        print(f"{name}: {details['stock']}")

if __name__ == "__main__":
    main()
