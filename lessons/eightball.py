"""A magic eight ball oracle of truth about the future."""

from random import randint 

input("Ask a yes or no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Yes, definitly!")
elif response == 1:
    print("looking hopeful. ")
elif response == 2:
    print("ask again later. ")
else:
    print("no way! ")
