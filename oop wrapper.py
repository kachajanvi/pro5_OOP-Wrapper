#employee management system using oop
#person class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_detail(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.salary = salary

    def show_detail(self):
        super().show_detail()
        print(f"Emp ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        
class manager(Employee):
    def __init__(self,name,age,emp_id,salary,department):
        super().__init__(name,age,emp_id,salary)
        self.department = department

    def show_detail(self):
        super().show_detail()
        print(f"Department: {self.department}")
        
class developer(Employee):
    def __init__(self,name,age,emp_id,salary,language):
        super().__init__(name,age,emp_id,salary)
        self.language = language

    def show_detail(self):
        super().show_detail()
        print(f"language: {self.language}")

#store data in list
Employees=[]

while True:
    print("\n=====EMPLOYEE SYSTEM=====")
    print("1.Add Person")
    print("2.Add Employee")
    print("3.Add Manager")
    print("4.Add Developer")
    print("5.Show All Employee")
    print("6.SEarch by Name")
    print("7.Exit")

    choice=input("Enter choice:")

    if choice == "1":
        name = input("Name:")
        age = int(input("Age:"))
        p = person(name,age)
        Employees.append(p)
        print("person added!")

    elif choice == "2":
        name = input("Name:")
        age = int(input("Age:"))
        emp_id = input("Emp ID:")
        salary = int(input("salary:"))
        e = Employee(name,age,emp_id,salary)
        Employees.append(e)
        print("Employee added!")

    elif choice == "3":
        name = input("Name:")
        age = int(input("Age:"))
        emp_id = input("Emp ID:")
        salary = int(input("salary:"))
        department = input("Department:")
        m = manager(name,age,emp_id,salary,department)
        Employees.append(m)
        print("manager added!")

    elif choice == "4":
        name = input("Name:")
        age = int(input("Age:"))
        emp_id = input("Emp ID:")
        salary = int(input("salary:"))
        language = input("language:")
        d = developer(name,age,emp_id,salary,language)
        Employees.append(d)
        print("developer added!")

    elif choice == "5":
        if len(Employees) == 0:
            print("No data yet")
        else:
            for emp in Employees:
                emp.show_detail()
            print("--------------")
                
    elif choice == "6":
        search = input("Enter name to search:")
        found = False
        for emp in Employees:
            if emp.name.lower() == search.lower():
               emp.show_detail
               found = True
            print("----------------")

            if not found:
                print("Name not found")
                
    elif choice == "7":
        print("Exit")
        break

    else:
        print("Invalid choice!")
