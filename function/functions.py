#! sum of two numbers
# def sum(num1, num2):
#     if type(num1 is not int or type(num2) is not int):
#         return

#     return num1 + num2


# total = sum("5", 7)
# print(total)


#! multiply two numbers
# def multiply_items(*args):  # * we can define any name as a parameter
#     print(args)
#     print(type(args))


# multiply_items("Hemlal", "Dulal")


def mult_name_items(**swara):
    print(swara)
    print(type(swara))


mult_name_items(first="Hemlal", last="Dulal")  # * it is treated as dictionaries
