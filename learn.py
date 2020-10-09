# x = 10
# if not x > 10:
#     print("retured True")
# else:
#     print("retured False")


# x = 10
# if not x:
#     print("Evaluated True")
# else:
#     print("Evaluated False")


# A demo of Python 'not' with 'in' operator
a_List = [5, 10, 15, 20, 25, 30]

for a in a_List:
    if not a in (10, 25):
        print("List Item: ", a)