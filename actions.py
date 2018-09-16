# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "NeverEnough.com"  # Give your site a name

def welcome():
    print("\nWelcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for store in stores :
        print( "- %s" % store.name)


def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for st in stores:
        if st.name.lower() ==  store_name.lower():
            return st
    return False

    



def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    print("\nPick a store by typing its name.\nYou can type \"checkout\" to pay your bills :] ")
    while True:
        store_name = input("Enter here: ")
        if store_name.lower() == "checkout":
            return False
        elif False == get_store(store_name) :
            print("No store with that name. Please try again.")
            continue
        else :
            return get_store(store_name)
    


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    print("="*20)
    print("%s: " % picked_store.name)
    picked_store.print_products()

    print("\nPick the items you want to add to the cart by typing its name exactly as it was spelled. \nOr type \"back\" to go back to the main menu.")
    print("\nYou can type \"checkout\" to pay your bills from here also :D ")

    while True:
        userInputItem = input("Enter here: ").lower()
        if userInputItem == "back" :
            return False
        elif userInputItem == "checkout" :
            return True
        elif [ True for x in picked_store.products if  x.name.lower() == userInputItem] :
            for x in picked_store.products : 
                if  x.name.lower() == userInputItem :
                    cart.add_to_cart(x)
                    print("Added!!")
                    break
        else :
            print("invalid input, please try again.")
            continue


        
    

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    checked = False

    while True :
        if checked == False:
            picked = pick_store()
        elif checked == True:
            if cart.checkout() == True :
                break
            else :
                checked = False
                continue

        if picked == False :
            if cart.checkout() == True :
                break
            else :
                continue
        else :
            checked = pick_products(cart, picked)



def thank_you():
    print("Thank you for shopping with us at %s, don't come again..." % site_name)
