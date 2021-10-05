# variables
list = []

# oprations on list
def printList():
	print(list)

def add(data):
	list.append(data)

def remove(loc):
	i=loc-1
	del list[i]

def update(loc,data):
	i=loc-1
	list[i]=data
	

print("Please enter the task to add ")
#task_input=input("")
# add(task_input)
add("Wash clothes")
add("Read Books")
add("Finish the python assignment")

printList()

remove(2)
printList()

update(2,"Finish the math assignment")
printList()
