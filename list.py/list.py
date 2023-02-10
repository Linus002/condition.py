# my first python list 
numbers = [45, 67, 34, 67]
names = ("python", "java", "typescript")

print(len(numbers)) # get the length on my list

for i in range(len(numbers)):
    print(numbers[i])

    #list methods

    #Index
    print(names.index("python"))

    #Append
    #before appending 
    for i in range(len(numbers)):
        print(numbers[i])

    print("/n")
    numbers.append(90)

    #after appending
    for i in range(len(numbers)):
        print(numbers[i])


    #sort - arranges list in ascending order
    for i in range(len(numbers)):
        print(numbers[i])

    # sort the list
    numbers.sort()

    #count
    #element
    print(numbers.count(67))


    #pop - removes an element at a given index and returns that element
    print(numbers.pop(2))

    #insert - inserts an element x at an index yand returns that element
    numbers.insert(2, 100) 

    for i in range(len(numbers)):
        print(numbers[i])


    #remove 
    #tips and tricks

    #multiplying a list
    zero = [0] * 50
    finallist = zero + numbers
    numbers[2:]
    max(numbers)
    min(numbers)
    print(finallist)
    print(zero)
    print(numbers[2:])
    print(max(numbers))

# creating lists
num = []

for i in range(10):
    # insert elements into the list
    num.append(i)
for i in range(len(num)): 
    print(num[i])

 #EXERCISES
#create a list of even numbers
even_num = []

for num in range(20):
    if(num % 2 ==0):
        even_num.append(num)

for i in range(len(even_num)):
    print(even_num[i])