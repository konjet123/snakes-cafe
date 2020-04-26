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
food_list = {
        "Appetizers": {
            "Wings": 0,
            "Cookies": 0,
            "Spring Rolls": 0
        },
        "Entries": {
            "Salmon": 0,
            "Steak": 0,
            "Meat tornado": 0,
            "A literal garden": 0
        },
        "Deserts": {
            "Ice cream": 0,
            "Cake": 0,
            "Pie": 0,
        },
        "Drinks": {
            "Coffee": 0,
            "Tea": 0,
            "Unicorn tears": 0
        },
    }

def display_menu():
    for menu in food_list:
        print(dedent(f"""{menu}"""))
        for key, value in food_list[menu].items():
            print(key)

def process_menu(menu_order):
    flag = False
    for menu in food_list:
        current_menu = food_list[menu]
        menu_order = menu_order.title()        
        if menu_order in current_menu.keys():
            quantity = current_menu[menu_order]
            quantity = quantity +1
            current_menu[menu_order] = quantity
            print(f"Item Ordered {menu_order} with quantity {quantity}")
            flag = True
            return flag

if __name__ == '__main__':
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