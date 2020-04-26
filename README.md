from textwrap import dedent

title_message="""*************************************************
** Welcome to the Snakes Fafe **
*************************************************"""

order_message="""***************************
** What would like to order today **
***************************"""

error_message = """
******************************
** This item does not exist. Please enter a valid item from the menu **
******************************
"""


#creation of collection
food_list = [
    {
        
        "Name" : "appetizer_list",
        "Items" : [
            "wings",
            "cookies",
            "spring Rolls",
        ],
    },

    {
        "Name" : "entries_list",
        "Items" : [
            "salmon",
            "steak",
            "meat tornado",
            "a literal garden",
        ],
    },

    {
        "Name" : "desert_list",
        "Items" : [
            "ice cream",
            "cake",
            "pie",
        ],

    },
    {
        "Name" : "drinks_list",
        "Items" : [
            "coffee",
            "tea",
            "unicorn tears",
        ],
    },
]

def display_menu():
    for menu in food_list:
        pring(dedent(f"""{}***"""))

def process_menu(menu_order):
    flag = false
    For menu in food_list:
        current_menu = food_list[menu]
        menu_order = menu_order.title()        
        if menu_order in current_menu.keys():
            quantity = current_menu[menu_order]
            quantity = quantity +1
            current_menu[menu_order] = quality
            print(f"Item Ordered {menu_order} with quantity {quantity})
            flag = True
            return flag

if __name__ == '__main_':
    print(title_message)
    display_menu()
    input_val = input(order_message)
    while  input_val != "quit":
        flag = process_menu(input_val)
        if (flag):
            input_val = input(order_message)
        else:
            print(error_message)
            input_val = input(order_message)