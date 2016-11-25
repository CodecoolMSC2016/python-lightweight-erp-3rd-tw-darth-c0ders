# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
def start_module():
    
    handle_menu_hr()
    choose_hr()

    

    pass


# print the default table of records from the file
#
# @table: list of lists
def choose_hr():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("./hr/persons.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("./hr/persons.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file("./hr/persons.csv"),ui.get_inputs(["Enter id: "], ""))
    elif option == "4":
        update(data_manager.get_table_from_file("./hr/persons.csv"),ui.get_inputs(["Enter id: "], ""))
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        get_average_by_manufacturer(table, manufacturer)
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")

def handle_menu_hr():
    options = ["Show table",
               "Add new record",
               "Remove record",
               "Update record",
               "Get counts by manufacturers",
               "Get average by manufacturer"]

    ui.print_menu("HR menu", options, "Exit program")




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
    data_manager.write_table_to_file("./hr/persons.csv", table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    for column in range(len(table)):
        if table[column][0] == id_:
            table.pop(column)
    data_manager.write_table_to_file("./hr/persons.csv", table)

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

    data_manager.write_table_to_file("./hr/persons.csv", table)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
