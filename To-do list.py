# To-do list code
def task():
     tasks = []# This is empty list
     print("----WELCOME TO THE TO-DO LIST---")
    
    #  How many task perfome of user 
total_task = int(input("Enter how many task you want to add ="))
for i in range (1, total_task +1):

        task_name = input(f"Enter task {i} =")                                                                                                                                                                              
        #  enter task 
        task.append(task_name)          

print(f"Today's tasks are \n{task}")

while True:
     operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/")) 
# This is add operation
     if operation == 1:
          add = input("Enter task you want to add =")                                                   
          task.append(add)                                             
          print(f"Task {add} has been successfuly added----")
          due_date = input("Enter due date (YYYY-MM-DD): ")
# This is update operation  
     elif operation == 2:
          updated_val = input("Enter the task name you want to update =")
          if updated_val in task:
               up = input("Enter new task =")
               ind = task.index(updated_val)
               task[ind] = up
               print(f"Updated task{up}")
               due_date = input("Enter new due date (leave blank to keep current): ") 
# This is delete opreation
     elif operation == 3 :
          del_val = input("Which tasl you want to delete =")
          if del_val in task :
               ind = task.index(del_val)
               del_val[ind]
               print(f"task {del_val} has been deleted.....")
# 4 & 5 are task and programing closing operation
     elif operation == 4 :
          print(f"total task={task}")

     elif operation == 5 :
          print("closing the program...")
          break
# if you select any another task so this show invalid input
     else:
          print("Invalid input")


          task()

  

                      