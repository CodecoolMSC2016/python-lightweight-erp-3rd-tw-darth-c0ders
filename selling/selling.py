# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def choose_selling():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("./selling/sellings.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("./selling/sellings.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file("./selling/sellings.csv"),ui.get_inputs(["Enter id: "], ""))
    elif option == "4":
        update(data_manager.get_table_from_file("./selling/sellings.csv"),ui.get_inputs(["Enter id: "], ""))
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        get_average_by_manufacturer(table, manufacturer)
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")

def handle_menu_selling():
    options = ["Show table",
               "Add new record",
               "Remove record",
               "Update record",
               "Get counts by manufacturers",
               "Get average by manufacturer"]

    ui.print_menu("Selling manager menu", options, "Exit program")


def start_module():

    handle_menu_selling()
    choose_selling()


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    inputs = ui.get_inputs(["Enter new record(Title, Publisher, Price, In stock): "], "")
    inputs = inputs.split(",")
    game_row = []
    game_row.append(common.generate()) 
    game_row.append(inputs[0])
    game_row.append(inputs[1])
    game_row.append(inputs[2])
    game_row.append(inputs[3])
    table.append(game_row)
    data_manager.write_table_to_file("./selling/sellings.csv", table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    for column in range(len(table)):
        if table[column][0] == id_:
            table.pop(column)
    data_manager.write_table_to_file("./selling/sellings.csv", table)

    return table



# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    selected_id = ""
    for column in table:
        if column[0] == id_:
            selected_id = column[0]

    inputs = ui.get_inputs(["Enter new values(Title, Publisher, Price, In stock): "], "")
    inputs = inputs.split(",")

    game_row = []
    game_row.append(selected_id) 
    game_row.append(inputs[0])
    game_row.append(inputs[1])
    game_row.append(inputs[2])
    game_row.append(inputs[3])

    for column_id in range(len(table)):
        if table[column_id][0] == selected_id:
            table[column_id] = game_row

    data_manager.write_table_to_file("./selling/sellings.csv", table)

    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):

    # your code

    pass


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
