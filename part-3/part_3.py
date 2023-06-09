my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_info(book):
    title, author, year, rating, pages = book["title"], book["author"], book["year"], book["rating"], book["pages"]

    return (f"{title} was written by {author} and was first published in {year}. It is {pages} long and has an average rating of {rating}.")
    
# print(book_info(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(book):
    return book['title']

def book_author(book):
    return book["author"]

def book_rating(book):
    return book['rating']

# print(book_title(my_book))
# print(book_author(my_book))
# print(book_rating(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
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

#If you want to read something, but don't want it to take long.
def shortest_read(ls):
    shortest_book = None
    num_of_pages = 999999
    for book in ls:
        if book['pages'] < num_of_pages:
            num_of_pages = book['pages']
            shortest_book = book['title']
    return f"The shortest book in your library is {shortest_book} at {num_of_pages} pages."


#List of all the titles in your library
def all_titles(ls):
    titles_list = []
    for book in ls:
        titles_list.append(book['title'])
    return titles_list


#Gives books above or equal to a certain rating specified by the user.

def above_rating(rating,ls):
    rating_ls = []

    for book in ls:
        if book['rating'] >= rating:
            rating_ls.append((book['title'], book['rating']))
    return rating_ls



# print(shortest_read(book_list))
# print(all_titles(book_list))
# print(above_rating(4.5, book_list))