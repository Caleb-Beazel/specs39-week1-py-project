### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Creates library.txt
# with open("library.txt", "w") as f:
#     f.write("title, author, year, rating, pages\n")
# def add_book():
#     title = input("Please enter a title: ")
#     author = input("Please provide an author: ")
#     try:
#         year = int(input("provide a year of publication: "))
#     except:
#         year = int(input("provide a year of publication: "))
#     try:
#         rating = float(input("Please provide a rating between 1 and 5: "))
#     except:
#         rating = float(input("Please provide a rating between 1 and 5: "))
#     try:
#         pages = int(input("Please provide the number of pages: "))
#     except:
#         pages = int(input("Please provide the number of pages: "))
        

#     with open("library.txt", "a") as f:
#         f.write(f"{title}, {author}, {year}, {rating}, {pages} \n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
# def show_library():
#     library_list = []
#     with open("library.txt", "r") as f:
#         file = f.readlines()

#         for line in file:
#             line = line.split(',')

#             book_dictionary = {
#             "title" : line[0],
#             "author" : line[1],
#             "year" : line[2],
#             "rating": line[3],
#             "pages" : line[4]
#             }

#             library_list.append(book_dictionary)

#     return library_list

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def main_menu():
    exit_menu = False
    while exit_menu == False:
        menu = input("\nShow all books - 'list'\nAdd a book - 'add'\nRecommend a random book - 'rec'\nTitles A-Z - 'titles'\nSearch Library - 'search'\nQuit book app - 'quit' ")
        if menu == 'list':
            print(show_library())
            input("Hit enter to retun to main menu... ")
        elif menu == 'add':
            add_book()
            print('-----------------')
            print(show_library())
            print('-----------------')
            input("Hit enter to retun to main menu... ")
        elif menu == 'rec':
            print('-----------------')
            print(suggest_book())
            print('-----------------')
            input("Hit enter to retun to main menu... ")
        elif menu == 'titles':
            a_z_titles = list_titles()
            print('-----------------')
            for title in a_z_titles:
                print(title)
            print('-----------------')
            input("Hit enter to retun to main menu... ")  
        elif menu == 'search':
            print('-----------------')
            print(search_library())
            print('-----------------')
            
        elif menu == 'quit':
            exit_menu = True

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def show_library():

    library_list = []
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            line = line.split(',')

            book_dictionary = {
            "title" : line[0],
            "author" : line[1],
            "year" : line[2],
            "rating": line[3],
            "pages" : line[4]
            }

            library_list.append(book_dictionary)

    return library_list

def add_book():
    title = input("Please enter a title: ")
    author = input("Please provide an author: ")
    try:
        year = int(input("provide a year of publication: "))
    except:
        year = int(input("provide a year of publication: "))
    try:
        rating = float(input("Please provide a rating between 1 and 5: "))
    except:
        rating = float(input("Please provide a rating between 1 and 5: "))
    try:
        pages = int(input("Please provide the number of pages: "))
    except:
        pages = int(input("Please provide the number of pages: "))
        

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages} \n")

def suggest_book():
    import random
    random_book = random.choice(show_library())
    return random_book

def list_titles():
    titles = []
    library_list = show_library()
    for book in library_list:
        titles.append(book['title'])

    titles.sort()
    return titles

def search_library():
    library_list = show_library()
    search_list = []
    search = input("Search library by title, or author ")

    for book in library_list:
        if search.lower() in book['title'].lower() or search.lower() in book['author'].lower():
            search_list.append(book)

    return search_list


if __name__ == "__main__":
    main_menu()