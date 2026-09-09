products = []

while True:
    item = input("Товар: ")

    if item == "стоп":
        break

    products.append(item)

print(products)