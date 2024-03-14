import dbal
from model import student
command = input('Enter Get or Add or Delete or Update')
if command == 'Get':
    rows = dbal.Getstudent()
    for row in rows:
        print(row)
    
elif command == 'Add':
    objData = student()   #create a class object    
    objData.Rollno = int(input("Enter Rollno:"))
    objData.fname = input("Enter fname:")
    objData.lname = input("Enter lname: ")
    objData.subject = input("Enter subject: ")
    objData.marks = int(input("Enter marks:"))
    objData.city = input("Enter city: ")
    objData.address = input("Enter address: ")
    objData.zipcode = int(input("Enter zipcode: "))

    dbal.Addstudent(objData)
    #with the help object objData of student() class we are populating or initializing the values of student class

    
elif command == 'Delete':
    RollnoToDelete = input('enter rollno of the row you want to delete :')
    dbal.Delete(RollnoToDelete)
    print("row successfully deleted")
####elif:
##    print('Enter a valid Command')

elif command == 'Update':
     studentRollno = int(input("Enter Requiredrollno: "))
     objData = dbal.GetstudentByRollno(studentRollno)
     print()
     print('---ENter Updation details---')
     print()
     
     objData.fname = input("Enter Updated fname: ")
     objData.lname = input("Enter Updated lname: ")
     objData.subject = input("Enter  Updated subject: ")
     objData.marks = int(input("Enter Updated marks: "))
     objData.city =   input("Enter Updated city: ")
     objData.address = input("Enter  Updated Address: ")
     objData.zipcode = int(input("Enter Updated zipcode:"))

     dbal.Updatestudent(objData)
     

    
    
