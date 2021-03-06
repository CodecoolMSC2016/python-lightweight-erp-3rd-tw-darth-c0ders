

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table


#def print_table(table, title_list):
#    max_column_lenght = 0
#    
#    for row in table:
#        print_column = ""
#        for column in row:
#            if max_column_lenght < len(column):
#                max_column_lenght = len(column)
#        for column in row:     
#            a = max_column_lenght
#            b = a - len(column)
#            c = (b/2) + 2
#
#            print_column += " "*int(c) + column + " "*int(c)
#            
#        print(print_column)
#        max_column_lenght = 0
#    pass

def print_table(table, title_list):
    line = ""
    for row in table:
        for column in row:
            line = line + "--" + column
        print(line)
        line = ""



# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    print(label)
    for i in result:
        print(i)

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):

    print(title)
    for i in range(0,len(list_options)):
        print("(" + str(i+1) + ") " + list_options[i])
    print("(0) " + exit_message)


    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    inputs = input(list_labels[0])

    # your code

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print(message)

    pass

def text_format():
    
    pass