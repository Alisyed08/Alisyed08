#This code counts the number of given numbers, their sum,
minimum and their mean
#Values must entered as the next example: 4 6 -1
# In first 5 lines we create our list
list_a = []
list_a = [int(item) for item in input("Enter the list items :
").split()]
for i in list_a:#This part it checks if there is a -1 in the
list. If list has -1 it removes it.
    if i==-1:
        list_a.remove(i)
number_of_elements = len(list_a)#This part counts the number
of elements
if number_of_elements == 0:#This part gives value if there is
no element in the list
    print("m=-1, a=-1")
total=0 #This part calculates the sum of the elements
for ele in range(0, len(list_a)):
    total = total + list_a[ele]
if number_of_elements != 0: #This part calculates the mean
    a=total/number_of_elements
list_a.sort() #This part finds the minimum value
if number_of_elements > 1:
    print("n = ",number_of_elements,", s = ",total,", m =
",*list_a[:1],", a = ",a,)
