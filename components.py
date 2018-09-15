# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products=[]

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        for prod in self.products:
            print(prod)
            print()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name 
        self.description = description
        self.price = price

    def __str__(self):
        return "\tProduct Name: %s\n\tDescription: %s \n\tPrice: %s KWD" % (self.name, self.description, self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0
        for pr in self.products:
            total += pr.price

        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("~-"*10)
        print("Here's your receipt OwO!!")
        for x in self.products:
            print(x)
            print()
        print("Your total is: %s" % self.get_total_price())

    def checkout(self):
        """
        Does the checkout.
        """
        self.print_receipt()
        while True:
            answer = str(input("Confirm?(yes/no)")).lower()
            if answer == "yes":
                return True
            elif answer == "no":
                return False
            else:
                print("invalid input.")
                continue
