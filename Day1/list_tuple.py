A = input("Enter your first favorite movie: ")
B = input("Enter your second favorite movie: ")
C = input("Enter your third favorite movie: ")

movies = [A,B,C]

print("Your favorite movies are: ", movies)

pallindrome = movies[::-1]

if (pallindrome == movies):
    print("Your favorite movies list is a palindrome")
else:
    print("Your favorite movies list is not a palindrome")


tuple = (A,B,A,A,B,C,C,C,A,A,B,C,C,C,A,A,B,C,C,C)

print("The no. of A in the tuple is: ", tuple.count(A))

list1 = list(tuple)
list1.reverse()
print (list1)
