### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def new_book():

#     title = input("Title: ")
#     author = input("Author: ")
#     year = input("Year of Publication: ")
#     rating = input("Rating: ")
#     pages = input("Number of Pages: ")

#     new_book_obj = {
#         "title" : title,
#         "author" : author,
#         "year" : year,
#         "rating": rating,
#         "pages" : pages
#     }

#     return new_book_obj

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def new_book():

#     title = input("Title: ")
#     author = input("Author: ")
#     year = int(input("Year of Publication: "))
#     rating = float(input("Rating: "))
#     pages = int(input("Number of Pages: "))

#     new_book_obj = {
#         "title" : title,
#         "author" : author,
#         "year" : year,
#         "rating": rating,
#         "pages" : pages
#     }

#     return new_book_obj


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def new_book():



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
        

    book_dictionary = {
        "title" : title,
        "author" : author,
        "year" : year,
        "rating": rating,
        "pages" : pages
    }

    return book_dictionary




### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
book_list =[{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},{
    "title": "Man's Search For Meaning",
    "author": "Viktor E. Frankl",
    "year": 1959,
    "rating": 5,
    "pages": 144
},{
    "title": "Endurance",
    "author": "Alfred Lansing",
    "year": 1959,
    "rating": 4.8,
    "pages": 353
}]


# def main_menu():
    
#     menu = input("Show all books - 'list'   Add a book - 'add' ")
#     if menu == 'list':
#         print(book_list)
#         to_main = input("Return to main menu? 'y' ")
#         if to_main == 'y':
#             main_menu()
#     elif menu == 'add':
#         book_list.append(new_book())
#         print(book_list)
#         to_main = input("Return to main menu? 'y' ")
#         if to_main == 'y':
#             main_menu()
        
# main_menu()
#     title = None
#     author = None
#     year = None
#     rating = None
#     pages = None
#  
# if isinstance(year, int) == False:
            # print("You must provide a year in numbers")


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu():
    exit_menu = False
    while exit_menu == False:
        menu = input("Show all books - 'list'   Add a book - 'add'   Quit book app - 'quit' ")
        if menu == 'list':
            print(book_list)
            input("Hit enter to retun to main menu... ")
        elif menu == 'add':
            book_list.append(new_book())
            print(book_list)
            input("Hit enter to retun to main menu... ")
            
        elif menu == 'quit':
            exit_menu = True
        
main_menu()
