### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Alfred Lansing", "David McCullough", "Brandon Sanderson", "J K Rowling", "Viktor Frankl", "Ralph Waldo Emerson", "James Clear"]

# Now let's add a new author to the end with the .append() method. Type your code below.
# Code here
# Example: my_authors.append("H.G. Wells")

my_authors.append("Brene Brown")

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")

my_authors.remove("Brene Brown")

# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]

my_authors[0]

# Now slice the list.

# Code here
# Example: my_authors[1:4]

my_authors[2:5]

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")

author_tuple = ("Alfred Lansing", "David McCullough", "Brandon Sanderson", "J K Rowling", "Viktor Frankl", "Ralph Waldo Emerson", "James Clear")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}

author_set = {"Alfred Lansing", "David McCullough", "Brandon Sanderson", "J K Rowling", "Viktor Frankl", "Ralph Waldo Emerson", "James Clear"}
# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")

author_set.add("Brene Brown")

# Try adding the same author again, and be sure to print your set.


# Code here
# Example: my_author_set.add("J.R.R. Tolkien")

author_set.add("Alfred Lansing")
# print(author_set)


### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)
for book in  my_authors:
    print(book)

print('----------------------')
# for book in my_authors_tuple:
    # print(book)
for book in author_tuple:
    print(book)

print('----------------------')
# for book in my_authors_set:
    # print(book)
for book in author_set:
    print(book)

