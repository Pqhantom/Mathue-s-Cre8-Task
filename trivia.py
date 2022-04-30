import random

qadb = []
qadb.append({
  "Question": "What animal goes Meow?",
  "Answer": "cat"
})
qadb.append({
  "Question": "What animal goes Moo?",
  "Answer": "cow"
})
qadb.append({
  "Question": "What animal goes woof?",
  "Answer": "dog"
})
# ~~~~~  This is a tester to print the Answer Key in the terminal ~~~~~

# def printing(n): # this printes the code with the format given 
#   print(qadb[n]["Question"])
#   print(qadb[n]["Answer"])
              
# def aba(): #simple function that prints out all of the Q&A entries 
#   for n in range(len(qadb)):
#     printing(n)

def brain():
  n = random.randint(0, 2)
  question = qadb[n]["Question"]
  print(n)
  print(question)
 

brain()