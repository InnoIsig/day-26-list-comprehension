# numbers = [1, 2, 3, 4]
# news_list = [n + 1 for n in numbers]
# print(f"New list is : {news_list}")

range_liste = [num * 2 for num in range(1, 5)]
print(range_liste)

#Exercice 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

#Exercice 2
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for  number in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)

#Exercice 3
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