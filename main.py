class Book:
  # Init the book attributes so that other methods can access them
  def __init__(self, title, author, shelf):
    self.title = title
    self.author = author
    self.shelf = shelf
  # Print the book attributes for display in console
  def display(self):
    print("-----------------")
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"Shelf: {self.shelf}")
    print("-----------------")

#Store an array of books OUTSIDE the options function so that it
#can save books while the program is running 
arr = []
def options():
  inpt = input(
      "What would you like to do?\n1. Add a book\n2. Search for a book\n3. Exit\n\n - "
  )
  # Check the inputs to see what option the user chose
  # If the user chose 1, add a book
  # If the user chose 2, search for a book
  # If the user chose 3, exit the program
  if inpt == "1":
    title = input("What is the title of the book?\n\n - ")
    author = input("Who is the author of the book?\n\n - ")
    shelf = input("What is the shelf of the book?\n\n - ")
    arr.append(Book(title, author, shelf))
    options()
  elif inpt == "2":
    search = input(
      "Enter a search term, you can search for the book name, author, or shelf\n\n - "
                  )
    # If no search term is provided loop through all books and 
    # output them to the console.
    if search == "":
      for i in arr:
        i.display()
      options()
      return
    else:
      # If the user did not hit enter and entered a search
      # User a for loop to loop through all books and check if the
      # search term is in the book attributes if so, display them
      for i in arr:
        if (
            search.lower() in i.title.lower() 
            or search.lower() in i.author.lower() 
            or search.lower() in i.shelf.lower()
        ):
          i.display()
          # If the search term is not in the book attributes, output no results found.
        else: 
          print("No results found\n")
          options()
          return
      options()
      return
    
  elif inpt == "3":
    # Before exiting the program, Output books in system.
    print("Books in system: \n")
    for i in arr:
      i.display()
    print("\nProgram Terminated!")
    return
options()