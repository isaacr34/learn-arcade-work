import arcade

"""
class Book():

    def __init__(self):
        self.title = ""
        self.author = ""
        self.pages = 0


def main():
    my_book = Book()
    my_book.pages = 295
    print(my_book.pages)


main()
"""
my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]

print(my_list)

temp = my_list[6]
my_list[6] = my_list[7]
my_list[7] = temp

print(my_list)

my_list = [27, 32, 18, 2, 11, 57, 14, 38, 19, 91]

print(my_list)

temp = my_list[0]
my_list[0] = my_list[3]
my_list[3] = temp

print(my_list)
