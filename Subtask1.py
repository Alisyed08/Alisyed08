#This code finds the largest square number which is smaller
than given number
n = int(input("Enter a number: ")) #This is the input part. It
takes the given string and turns it to integer.
q=1
while (n >= q*q): # This part finds the largest square number
which is smaller than the input
    q=q+1 #If the input is bigger that the q*q it increases q
by 1.
q=q-1 #When it finds the value for q which its square is
bigger than the input it reduces q by 1
print ("q = ",q*q)#Then it prints the result
