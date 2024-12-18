import os
#Define filepath to resource (txt-file)
file_path = 'Resources/input2.txt'
print('Current working directory', os.getcwd())
#print current working directory
#intialize to lists
list1 = []
list2 = []

#open file, split columns in two seperate lines and read the content in a list
with open(file_path, 'r') as file:
    for line in file:
        list1.append(line.strip().split()[0])
        list2.append(line.strip().split()[1])
#sort the list
list1.sort()
list2.sort()
print('Sorted list 1:', list1[:10])
#Ausgabe der ersten 10 Werte zum validieren ob Input funktioniert hat
print('Sorted list 2:', list2[:10])

#caluclate the difference of each element in the list and sum them up
result = sum([abs(int(a) - int(b))for a, b in zip(list1, list2)])
result2 = sum([int(a) * int(list2.count(a)) for a in list1])
print(result)
print(result2)




