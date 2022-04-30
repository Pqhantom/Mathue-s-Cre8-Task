qadb = []
qadb.append({
  "Question": "What animal goes Meow?",
  "Answer": "cat"
})
qadb.append({
  "Question": "What animal goes Moo?",
  "Answer": "cow"
})

def printing(n): # this printes the code with the format given 
  print(qadb[n]["Question"])
  print(qadb[n]["Answer"])
              
def aba(): #simple function that prints out all of the Q&A entries 
  for n in range(len(qadb)):
    printing(n)

