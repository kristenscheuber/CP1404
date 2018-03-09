'''
Do all of the following in a single file called files.py:
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that
name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt” (You can create a simple text file in PyCharm with Ctrl+N, choose
“File” and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
4. Extended (perhaps only do this if you’re cruising… if you are struggling, just read the solution) …
Now extend your program so that it can print the total for a file containing any number of numbers.
'''

#Task 1 - Ask for the users name and write it to the file.
out_file = open("name.txt", 'w')

user_name = input("Your Name: ")
print('{}'.format(user_name), file=out_file)

out_file.close()

#Task 2 - Read the users name and output this in a string.
out_file = open("name.txt", 'r')
for line in out_file:
    print("Your Name is", line)

#Task 3 - Create a numbers file and write two numbers two it
number_file = open("numbers.txt", 'w')

number_file.write("17\n")
number_file.write("42\n")

number_file.close()

number_file = open("numbers.txt", 'r')
number_1 = int(number_file.readline())
number_2 = int(number_file.readline())
total = number_1 + number_2
print(total)

number_file.close()
