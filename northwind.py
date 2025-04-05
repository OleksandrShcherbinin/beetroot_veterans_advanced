from northwind_models import Products


def main():
    for product in Products.select():
        print(product)


if __name__ == '__main__':
    main()
