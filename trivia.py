import random

qadb = [] # list
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

def brain():
  print("In order to prove your humanity please type the answer to the following question.")
  n = random.randint(0, 2)
  question = qadb[n]["Question"]
  x = input(question + "\n")
  checker(x, n, question) # call to procedure
 
def checker(x, n, question): # procedure with three parameters
  if x == qadb[n]["Answer"]: # selection
   print("C O N G R A T U L A T I O N S  Y O U  A R E  A  H U M A N !")
   quit()
   
  else: 
    while x != question: # iteration 
      print("Unfortunately you are a robot.")
      x = input(question + "\n") # sequencing
      checker(x, n, question)

brain()