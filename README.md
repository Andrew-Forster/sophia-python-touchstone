Name: Andrew Forster
Date: 6/16/24
Final Replit Program Share Link: Sophia Learning Python Touchstone - Replit
Complete the following template. Fill out all entries using complete sentences.

 
PART 1: Defining Your Problem

Task
State the problem you are planning to solve.

Requirements
●	Describe the problem you are trying to solve for.
●	Describe any input data you expect to use. 
●	Describe what the program will do to solve the problem. 
●	Describe any outputs or results the program will provide.

Inspiration
When writing your entry below ask yourself the following questions:
●	Why do you want to solve this particular problem?
●	What source(s) of data do you believe you will need? Will the user need to supply that data, or will you get it from an external file or another source?
●	Will you need to interact with the user throughout the program? Will users continually need to enter data in and see something to continue?
●	What are your expected results or what will be the end product? What will you need to tell a user of your program when it is complete?
<Write your journal entry response here>

I want to make a system that can store library books and say what shelf they are at within a system. For now, the user will manually supply the information/data so books can be tracked. The program will continually run in a while loop or Recursion until the user would like to kill the program. The end product should be a program where you can view inputted books with the shelf # in a pagination system.
 
PART 2: Working Through Specific Examples

Task
Write down clear and specific steps to solve a simple version of your problem you identified in Part 1.


Requirements
Complete the three steps below for at least two distinct examples/scenarios.
●	State any necessary input data for your simplified problem. 
●	Write clear and specific steps in English (not Python) detailing what the program will do to solve the problem. 
●	Describe the specific result of your example/scenario.

Inspiration
When writing your entry below ask yourself the following questions:
●	Are there any steps that you don’t fully understand? These are places to spend more time working out the details. Consider adding additional smaller steps in these spots.
●	Remember that a computer program is very literal. Are there any steps that are unclear? Try giving the steps of your example/scenario to a friend or family member to read through and ask you questions about parts they don’t understand. Rewrite these parts as clearly as you can.
●	Are there interesting edge cases for your program? Try to start one of your examples/scenarios with input that matches this edge case. How does it change how your program might work?
<Write your journal entry response here>

Scenario 1: A user would like to input a book

1.	Listen to the console for the user
2.	Request the book information
3.	Save the book information to a list or array.

Scenario 2: A user would like to view books in the system

1.	Listen to console for user response
2.	Request the user input a search term, if none given display all books
3.	Output the saved data in correspondence to the search term.
 
PART 3: Generalizing Into Pseudocode

Task
Write out the general sequence your program will use, including all specific examples/scenarios you provided in Part 2.

Requirements
●	Write pseudocode for the program in English but refer to Python program elements where they are appropriate. The pseudocode should represent the full functionality of the program, not just a simplified version. Pseudocode is broken down enough that the details of the program are no longer in any paragraph form.  One statement per line is ideal.

Help with writing pseudocode
●	Here are a few links that can help you write pseudocode with examples.  Remember to check out part 3 of the Example Journal Template Submission if you have not already.  Note: everyone will write pseudocode differently.  There is no right or wrong way to write it other than to make sure you write it clearly and in as much detail as you can so that it should be easy to convert it to code later.
○	https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/ 
○	https://www.wikihow.com/Write-Pseudocode 

Inspiration
When writing your entry below ask yourself the following questions:
●	Do you see common program elements and patterns in your specific examples/scenarios in Part 2, like variables, conditionals, functions,  loops, and classes? These should be part of your pseudocode for the general sequence as well.
●	Are there places where the steps for your examples/scenarios in Part 2 diverged? These may be places where errors may occur later in the project. Make note of them.
●	When you are finished with your pseudocode, does it make sense, even to a person that does not know Python? Aim for the clearest description of the steps, as this will make it easier to convert into program code later.
<Write your pseudocode here>
Class Book
   Def init()
       Set the name
       Set the Shelf #
       Set the Author
   
   Function Display Book
       Print the name
       Print the Shelf #
       Print the Author








Function Options() 
   Set Array;
   Set in = input()
   If IN === add a book
       Print “Please input Book name, shelf & author”
       Set in = input();
       Split the response into 3 vars or ask for all three in separate prints
       Set newBook equal to Book(name, shelf, author)
       Push / Append newBook to the array.
      Options()
   Else if In === view all books
       Print “Search for a book, press enter for all books:”
       Set in = input();
       If IN is nothing or whitespace
           For (book in Array)
                Book.display()
       Else If
           For (book in Array)
                If (book.name contains INPUT)
                     Book.display()
      Options()
   Else 
       For (book in Array)
                Book.display()


       
       

   

 
PART 4: Testing Your Program

Task
While writing and testing your program code, describe your tests, record any errors, and state your approach to fixing the errors.

Requirements
●	For at least one of your test cases, describe how your choices for the test helped you understand whether the program was running correctly or not.
For each error that occurs while writing and testing your code:
●	Record the details of the error from Replit. A screenshot or copy-and-paste of the text into the journal entry is acceptable.
●	Describe what you attempted in order to fix the error. Clearly identify what approach was the one that worked.

Inspiration
When writing your entry below ask yourself the following questions:
●	Have you tested edge cases and special cases for the inputs of your program code? Often these unexpected values can cause errors in the operation of your program.
●	Have you tested opportunities for user error? If a user is asked to provide an input, what happens when they give the wrong type of input, like a letter instead of a number, or vice versa?
●	Did the outcome look the way you expected? Was it formatted correctly? 
●	Does your output align with the solution to the problem you coded for?
<Record your errors and fixes here>

Tried to add a book a view books, however it did not save for some reason

1. Add a book
2. View all books
3. Exit1
What is the title of the book?t
Who is the author of the book?a
What is the shelf of the book?55
What would you like to do?
1. Add a book
2. View all books
3. Exit2
What would you like to do?
1. Add a book
2. View all books
3. Exit2

I fixed the issue by moving “arr = []” out of the scope of the options array because after the function recursion the data would be lost since arr[] was being initialized again after each recursion.


Had another issue where my program require exact casing and my program didn’t tell me if it didn’t find a result.

- 2
Enter a search term, you can search for the book name, author, or shelf

 - Geo
-----------------
Title: George
Author: bingo
Shelf: 55
-----------------
What would you like to do?
1. Add a book
2. Search for a book
3. Exit

 - 2
Enter a search term, you can search for the book name, author, or shelf

 - geo
What would you like to do?
1. Add a book
2. Search for a book
3. Exit

Both issues were fixed, added an else case if no matches were found and user .lower to lowercase both of the comparisons when searching for something.

PART 5: Commenting Your Program

Task
Submit your full program code, including thorough comments describing what each portion of the program should do when working correctly.

Requirements
●	The purpose of the program and each of its parts should be clear to a reader that does not know the Python programming language. 

Inspiration
When writing your entry, you are encouraged to consider the following:
●	Is each section or sub-section of your code commented to describe what the code is doing?
●	Give your code with comments to a friend or family member to review. Add additional comments to spots that confuse them to make it clearer.

