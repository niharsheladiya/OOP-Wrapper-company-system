# Welcome to OOP wrapper project

person = []
employees = []
managers = []
Developers = []




class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        if type(self) is Person:
            person.append({
                "Person Name" : self.name,
                "Person age" : self.age
            })

    def display(self):
        print(f"\nPerson Name : {self.name}\nAge: {self.age}")





    
class Employee(Person):
    
    # Constrator
    
    def __init__(self , employee_id, name, age, salary):

        super().__init__(name,age)
        self.__employee_id = employee_id
        self.__salary = salary
        

        if type(self) is Employee:
            employees.append({
                "Employee ID" : self.__employee_id,
                "Employee Name" : name,
                "Employee Age" : age,
                "Employee Salary" : self.__salary
            })


    def display(self):
        super().display()
        print(f"Emoplyee_ID : {self.__employee_id}\nSalary: ${self.__salary}")



    # Setter
    
    def set_emp_id(self , set_id):
        
        if self.__employee_id == set_id:
            self.__employee_id = int(input("Enter Update Employee ID : "))
            print(f"Empolyee ID {self.__employee_id} Updated Sucessfully.")
            
        else :
            print("This is Invaild ID.")



    # Setter
    
    def set_salary(self , set_salary):
        self.__salary = set_salary
        print(f"Employee Salary {self.__salary} Updated Sucessfully.")



    # Getter
    
    def get_emp_id(self):
        return print(f"Updated Employee ID : {self.__employee_id}")



    # Getter
    
    def get_salary(self):
        return print(f"Updated Salary : {self.__salary}")

    def __del__(self):
        emp_id = getattr(self, "_Employee__employee_id", "Unknown")
        print(f"Employee record [ID: {emp_id}] deleted.")





class Manager(Employee):

    def __init__(self, manager_id, name, age, salary, department):

        super().__init__(manager_id, name, age, salary)
        self.department = department

        if type(self) is Manager:
            managers.append({
                "ID" : manager_id,
                "Name" : name,
                "Age" : age,
                "Salary" : salary,
                "Department" : self.department
            })
            

    def display(self):
        super().display()
        print(f"Manager Department : {self.department}")


    def __del__(self):
        dept = getattr(self, "department", "Unknown")
        print(f"Manager record [Department: {dept}] deleted.")






class Developer(Manager):

    def __init__(self, developer_id, name, age, salary, department, languages):
        super().__init__(developer_id, name, age, salary, department)
        self.languages = languages

        if type(self) is Developer:
            Developers.append({
                "ID": developer_id,
                "Name": name,
                "Age": age,
                "Salary": salary,
                "Department": department,
                "Languages" : self.languages
            })
            

    def display(self):
        super().display()
        print(f"Developer Languages : {self.languages}")


    def __del__(self):
        langs = getattr(self, "languages", "Unknown")
        print(f"Developer record [Languages: {langs}] deleted.")

        



        
def Show_Details(records):
    
    if not records:
        print("No records found.")
        return
    
    for record in records:
        for key, value in record.items():
            print(f"{key} : {value}")
        print("-"*30)
        


print("Welcome to Python OOP Project: Company Management System.")

while True:

    print("\nChoose an operation :")
    print("\n 1. Create a Person ")
    print(" 2. Create an Employee ")
    print(" 3. Create a Manager ")
    print(" 4. Create a Developer ")
    print(" 5. Show Details ")
    print(" 6. Exit ")

    choice = int(input("\nEnter your choice:  "))

    match choice:
        
        case 1:
            
            name = input("Enter Person Name : ")
            age = int(input("Enter Person Age : "))
            per1 = Person(name , age)
            while True:
                
                print("\n 1. Display")
                print(" 2. Exit")
                choice_per = int(input("\n Enter Your choice : "))

                if choice_per == 1:
                    per1.display()
                    
                elif choice_per == 2:
                    print("\n Main menu")
                    
                    break
                else:
                    print("Enter Only 1 and 2 Number:")

                    
        case 2 :
            
            employee_id = int(input("\nEnter Employee ID : "))
            name = input("Enter Employee Name : ")
            age = int(input("Enter Employee Age : "))
            salary = float(input("Enter Employee Salary : "))

            emp1 = Employee(employee_id, name, age, salary)
            
            while True:
                
                print("\n 1. Update")
                print(" 2. Display")
                print(" 3. Display All Details")
                print(" 4. Exit ")
                choice_emp = int(input("\n Enter Your choice : "))

                if choice_emp == 1:
                    print("\n 1. Employee ID ")
                    print(" 2. Salary")
                    choice1 = int(input("\n Enter Update choice :"))
                    
                    if choice1 == 1:
                        emp_id = int(input("\n Check Employee ID :"))
                        emp1.set_emp_id(emp_id)
                        
                    elif choice1 == 2:
                        emp_salary = float(input("\n Update Employee Salary :"))
                        emp1.set_salary(emp_salary)
                        
                    else:
                        print("\n Choice Only 1 and 2 Number. ")
                        
                elif choice_emp == 2:
                    print("\n 1. Employee ID ")
                    print(" 2. Salary")
                    choice2 = int(input("\n Enter Display choice : "))
                    
                    if choice2 == 1:
                        emp1.get_emp_id()
                        
                    elif choice2 == 2:
                        emp1.get_salary()
                        
                    else:
                        print("\n Choice Only 1 and 2 Number.")
                        
                elif choice_emp == 3:
                    emp1.display()
                    
                elif choice_emp == 4:
                    print("Main Menu ")
                    
                    break
                else:
                    print("Enter Only 1 to 4 Number")
                    
                    
        case 3 :
            
            manager_id = int(input("\nEnter Manager ID : "))
            name = input("Enter Manager Name : ")
            age = int(input("Enter Manager Age : "))
            salary = float(input("Enter Manager Salary : "))
            department = input("Enter Manager Department : ")

            emp2 = Manager(manager_id, name, age, salary, department)
            
            while True:
                
                print("\n 1. Update  ")
                print(" 2. Display ")
                print(" 3. Display All Details  ")
                print(" 4. Exit ")

                choice_emp2 = int(input("\n Enter Your choice : "))
                
                if choice_emp2 == 1:
                    print("\n 1. Manager ID")
                    print(" 2. Salary")
                    choice3 = int(input("\n Enter Update choice :"))
                    
                    if choice3 == 1:
                        emp_id2 = int(input("\n Check Manager ID :"))
                        emp2.set_emp_id(emp_id2)
                        
                    elif choice3 == 2:
                        emp_salary2 = int(input("update Manager Salary : "))
                        emp2.set_salary(emp_salary2)
                        
                    else:
                        print("\n Only Enter 1 and 2 Number.")
                        
                elif choice_emp2 == 2:
                    print("\n 1. Display Manager ID ")
                    print(" 2. Display Salary ")
                    choice4 = int(input("\n Enter Display choice : "))
                    
                    if choice4 == 1:
                        emp2.get_emp_id()
                        
                    elif choice4 == 2:
                        emp2.get_salary()
                        
                    else:
                        print("\n  Choice Only 1 and 2 Number.")
                        
                elif choice_emp2 == 3:
                    emp2.display()
                    
                elif choice_emp2 == 4:
                    print("Main Menu")
                    
                    break
                else:
                    print("\n Enter Only 1 to 4 Numbers.")

            
        case 4 :
            
            developer_id = int(input("\nEnter Developer ID : "))
            name = input("Enter Developer Name : ")
            age = int(input("Enter Developer Age : "))
            salary = float(input("Enter Developer Salary : "))
            department = input("Enter Developer Department : ")
            languages = input("Enter Developer Languages : ")

            emp3 = Developer(developer_id, name, age, salary, department,languages)
            
            while True:
                
                print("\n 1. Update  ")
                print(" 2. Display ")
                print(" 3. Display All Details  ")
                print(" 4. Exit ")

                choice_emp3 = int(input("\n Enter Your choice : "))
                
                if choice_emp3 == 1:
                    print("\n 1. Developer ID")
                    print(" 2. Salary")
                    choice5 = int(input("\n Enter Update choice :"))
                    
                    if choice5 == 1:
                        emp_id3 = int(input("\n Check Developer ID :"))
                        emp3.set_emp_id(emp_id3)
                        
                    elif choice5 == 2:
                        emp_salary3 = int(input("Update Developer Salary : "))
                        emp3.set_salary(emp_salary3)
                        
                    else:
                        print("\n Only Enter 1 and 2 Number.")
                        
                elif choice_emp3 == 2:
                    print("\n 1. Display Developer ID ")
                    print(" 2. Display Salary ")
                    choice6 = int(input("\n Enter Display choice : "))
                    
                    if choice6 == 1:
                        emp3.get_emp_id()
                        
                    elif choice6 == 2:
                        emp3.get_salary()
                        
                    else:
                        print("\n  Choice Only 1 and 2 Number.")
                        
                elif choice_emp3 == 3:
                    emp3.display()
                    
                elif choice_emp3 == 4:
                    print("Main Menu")
                    
                    break
                else:
                    print("\n Enter Only 1 to 4 Numbers.")
                    

        case 5 :
            
            while True:
                
                print("\nChoose Details to show:")

                print("\n 1. Person")
                print(" 2. Employee ")
                print(" 3. Manager ")
                print(" 4. Developer ")
                print(" 5. Exit ")

                choice_4 = int(input("Enter Your Choice : "))
                
                match choice_4:
                    
                    case 1:
                        
                        if choice_4 == 1:
                            print("\n Person Details :")
                            Show_Details(person)
                            
                    case 2:
                        
                        if choice_4 == 2:
                            print("\n Employee Details :")
                            Show_Details(employees)
                            
                    case 3:
                        
                        if choice_4 == 3:
                            print("\n Manager Details :")
                            Show_Details(managers)
                            
                    case 4:
                        
                        if choice_4 == 4:
                            print("\n Developers Details :")
                            Show_Details(Developers)
                            
                    case 5:
                        
                        print("Main Menu")
                        break
                    
                    case _:
                        print("Enter Only 1 to 5 Numbers.")

                        
        case 6 :
            print(" Exit ")
 
            # use issubclass() only for external and it is check the class relationhip
            
            print("\n===== Class Heritical Checks (issubclass()) =====")
            print(f"Manager is a subclass of Employee   : {issubclass(Manager, Employee)}")
            print(f"Developer is a subclass of Manager  : {issubclass(Developer, Manager)}")
            print(f"Developer is a subclass of Employee : {issubclass(Developer, Employee)}")
 
            print("\nThank you for using the Company Management System. Goodbye!")
            break
        
        case _:
            print("Enter Only 1 To 6 Number. ")

    
