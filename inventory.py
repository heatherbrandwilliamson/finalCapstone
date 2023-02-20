
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#get cost function
    def get_cost(self):
        return self.cost

#get quantitiy function
    def get_quantity(self):
        return self.quantity

# return string rep of each class instance

    def __str__(self):
        return f"country: {self.country} code: {self.code} product: {self.product} cost: {self.cost} quantity: {self.quantity}"

#=============Shoe list===========

shoe_list = []

#The list will be used to store a list of objects of shoes.

#==========Functions outside the class==============
# open text file as CSV

def read_shoes_data(filename):
    try:
        f = open("inventory.txt", "r")
        contents = f.readlines()
        f.close()

        if len(contents) > 0:
            for line in contents:
                if contents.index(line) > 0:
                    country, code, product, cost, quantity = line.strip(). \
                        split(",")
                    line = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(line)
        else:
            print("\n\n➥ No data found in the file!\n Please ensure the file "
                  "you are using is populated with your stock data.")
            exit()

    except FileNotFoundError:
        print("➥ File not found!\n Please ensure you are using the correct "
              "file that contains your stock data")
        exit()


def capture_shoes(shoe_list):

    # request user input
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = input("enter the cost:")
    quantity = input("enter the quantity:")

    # create new class instance with user input and append to list
    shoe_list.append(Shoe(
        '\n' + country, code, product, cost, (quantity)
    ))

    # write the changes to inventory.txt
    write_txt(shoe_list)

def view_all():
    for i in shoe_list:
        print(i)

def re_stock():
    # using class method for quantity
    low = int(shoe_list[0].get_quantity())
    for index, i in enumerate(shoe_list):
        if int(i.get_quantity()) < low:
            low = int(i.get_quantity())
            low_index = index

    # get user input to add to quantity of lowest shoe
    # set default number to add to quantity
    max = 99
    stock = 0

    # show the user the shoe with the lowest quantity
    print(f"\nThe lowest stocked item is: {shoe_list[low_index]}")

    while stock <= 0 or stock > max:
        try:
            stock = int(input("\nPlease enter the quantity of stock you wish to add of this item: \n"))
            if stock > 99 or stock <= 0:
                print("\nOrder unacceptable.  Enter an integer between 1 and 99\n")

        # if input cannot be cast to int
        except ValueError:
            print("\nMake sure you enter an integer between 1 and 99\n")

    # change the quantity of the shoe at the selected index
    shoe_list[low_index].quantity = int(shoe_list[low_index].quantity) + stock

    # add the \n character to the new quantity
    shoe_list[low_index].quantity = str(shoe_list[low_index].quantity) + '\n'

    # update the text file with the new quantity
    write_txt(shoe_list)

# function to write new shoe_list to csv format text file, from a list of shoe objects
def write_txt(shoe_list):
    with open('inventory.txt', 'w') as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for i in shoe_list:
            f.write(f"{i.country},{i.code},{i.product},{i.cost},{i.quantity}")

# serach for a shoe in the shoe list, using the code as a search term
def search_shoe(shoe_list, search_code):
    for num, i in enumerate(shoe_list):
        if i.code == search_code.upper():
            return print("\n", shoe_list[num])

    print("\nShoe has not been found")

# print out the total value of inventory of each shoe
def value_per_item(shoe_list):
    for i in shoe_list:
        total = int(i.get_quantity()) * int(i.get_cost())

        print(f"\nThe total value of {i.product} is {total}")

# print the most numerous shoe
def highest_qty(shoe_list):
    # using class method for quantity
    high = int(shoe_list[0].quantity)
    for index, i in enumerate(shoe_list):
        if int(i.get_quantity()) > high:
            high = int(i.get_quantity())
            high_index = index

    print(f"\nThe {shoe_list[high_index].product} is the highest quantity of shoe in stock. We have {high} units in stock.\n")



#==========Main Menu=============

print("Choose an option from the menu below...")

selection = ''

# load the text file into the program
read_shoes_data('inventory.txt')

while selection != 'q':

    print("""
                    ╔═════════════════════════════╗
                    ║        Welcome to the       ║
                    ║ INVENTORY MANAGEMENT SYSTEM ║
                    ╚═════════════════════════════╝
        v - View All Stock
        s - Search by Code (input a code to search by)
        a - Add New Shoe to Stock List
        re - Re-Stock Lowest Item
        t - Get Total Value of each Shoe's inventory
        h - Get Highest Item in Stock
        q - quit program
\n""")

    selection = input("\nChoose an option from the menu: \n")

    if selection == 'v':
        view_all()

    elif selection == 's':
        code = input("\nEnter a code to search: \n")
        search_shoe(shoe_list, code)

    elif selection == 'a':
        capture_shoes(shoe_list)

    elif selection == 're':
        re_stock(shoe_list)

    elif selection == 't':
        value_per_item(shoe_list)

    elif selection == 'h':
        highest_qty(shoe_list)

    elif selection == 'q':
        print("\nQuitting Program\n")
        break

    else:
        print("\nSelection not recognised\n")