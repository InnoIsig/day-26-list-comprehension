# numbers = [1, 2, 3, 4]
# news_list = [n + 1 for n in numbers]
# print(f"New list is : {news_list}")

range_liste = [num * 2 for num in range(1, 5)]
print(range_liste)

#Exercice 1
"""
You are going to write a List Comprehension to create a new list called squared_numbers. 
This new list should contain every number in the list numbers but each number should be 
squared. 
e.g.
4 * 4 = 16
4 squared equals 16.
**DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop.
Target Output 
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025] 
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

#Exercice 2
"""
In this list comprehension exercise you will practice using list comprehension to filter 
out the even numbers from a series of numbers.   
First, use list comprehension to convert the list_of_strings to a list of integers 
called numbers.   
Then use list comprehension again to create a new list called result.
This new list should only contain the even numbers from the list numbers. 
Again, try to use Python's List Comprehension instead of a Loop. 
"""
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for  number in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)

#Exercice 3
"""

Data Overlap
💪 This exercise is HARD 💪 

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number 
on a new line. 
You are going to create a list called result which contains the numbers that are 
common in both files. 
e.g. if file1.txt contained: 

1 

2 

3

and file2.txt contained: 

2

3

4

result = [2, 3]
"""
# Ouvrir et lire les fichiers
with open('file1.txt', 'r') as file1:
    numbers1 = file1.read().splitlines()

with open('file2.txt', 'r') as file2:
    numbers2 = file2.read().splitlines()

# Convertir les chaînes de caractères en entiers
numbers1 = [int(num) for num in numbers1]
numbers2 = [int(num) for num in numbers2]

# Trouver les nombres communs
result = [num for num in numbers1 if num in numbers2]

# Afficher le résultat
print(result)