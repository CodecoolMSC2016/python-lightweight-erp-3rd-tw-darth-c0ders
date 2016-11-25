# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
def choose_tool():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("./tool_manager/tools.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("./tool_manager/tools.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file("./tool_manager/tools.csv"),ui.get_inputs(["Enter id: "], ""))
    elif option == "4":
        update(data_manager.get_table_from_file("./tool_manager/tools.csv"),ui.get_inputs(["Enter id: "], ""))
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        get_average_by_manufacturer(table, manufacturer)
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")

def handle_menu_tool():
    options = ["Show table",
               "Add new record",
               "Remove record",
               "Update record",
               "Get counts by manufacturers",
               "Get average by manufacturer"]

    ui.print_menu("Tool manager menu", options, "Exit program")


def start_module():

    handle_menu_tool()
    choose_tool()


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
    data_manager.write_table_to_file("./tool_manager/tools.csv", table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    for column in range(len(table)):
        if table[column][0] == id_:
            table.pop(column)
    data_manager.write_table_to_file("./tool_manager/tools.csv", table)

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

    data_manager.write_table_to_file("./tool_manager/tools.csv", table)

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
