import csv


class School:
    college_name = "Acropolis Institiute of Technology and Research"

    def __init__(self):
        self.rollno = ""
        self.name = ""
        self.batch = ""
        self.dob = ""
        self.contact = 0

    def inputdat(self):
        self.rollno = input("enter roll number : ")
        self.name = input("enter student name : ")
        self.batch = input("enter batch name : ")
        self.dob = input("enter date of birth : ")
        self.contact = int(input("enter contact number : "))
        print("registered !\n")

    def details(self):
        print("student name : ", self.name, " roll number : ", self.rollno, " batch : ", self.batch,
              " date of birth : ", self.dob, " contact : ", self.contact)

    def editrec(self):
        print("student name : ", self.name, " | roll number : ", self.rollno, " | batch : ", self.batch,
              " | date of birth(dob) : ", self.dob, " | contact : ", self.contact)
        cond = True
        while cond:
            commd=input("enter what you want to edit, type done to confirm : ")
            if commd == "name":
                self.name = input("enter student name : ")
            elif commd == "roll number":
                self.rollno = input("enter roll number : ")
            elif commd == "batch":
                self.batch = input("enter batch name : ")
            elif commd == "dob":
                self.dob = input("enter date of birth : ")
            elif commd == "contact":
                self.contact = int(input("enter contact number : "))
            elif commd == "done":
                    cond = False
            else :
                print("please, enter valid command\n ")
        print("done !! check by viewing it \n")

    def importcsv(self,dictemp):
        x=len(dictemp)
        dictemp[x] = dict()
        dictemp[x]["rollno"] = self.rollno
        dictemp[x]["name"] = self.name
        dictemp[x]["batch"] = self.batch
        dictemp[x]["dob"] = self.dob
        dictemp[x]["contact"] = self.contact
        field = ["rollno", "name", "batch", "dob", "contact"]
        filename = "studentrecord.csv"
        with open(filename, "a", newline="") as file:
            d_writer = csv.DictWriter(file, fieldnames=field)
            x = 0
            for x in range(len(dictemp)):
                d_writer.writerow(dictemp[x])
        return dictemp


condition = True
students = []
dictionary = dict()
x = 0
print("|welcome to student administration program|\n<WARNING : inport the data at last for data satblity>\n")
print("list of commands : \n"
      "1. help\n"
      "2. enter record\n"
      "3. edit record\n"
      "4. import to csv\n"
      "5. delete record\n"
      "6. view record\n"
      "7. exit\n")
command = ""
while condition:
    commnad=""
    command = input("command : ")
    if command == "help":
        print("list of commands : \n"
              "1. help\n"
              "2. enter record\n"
              "3. edit record\n"
              "4. import to csv\n"
              "5. delete record\n"
              "6. view record\n"
              "7. exit\n")

    if command == "enter record":
        print("enter student datails\n")
        students.append(School())
        students[len(students)-1].inputdat()

    if command == "edit record":
        rollnum = input("enter roll number : ")
        for x in students:
            if x.rollno == rollnum:
                x.editrec()
            else:
                print("roll number not found")

    if command == "delete record":
        rollnum = input("enter roll number : ")
        for x in students:
            if x.rollno == rollnum:
                students.remove(x)
                print("deleted !\n")
            else:
                print("roll number not found")

    if command == "view record":
        rollnum = input("enter roll number : ")
        for x in students:
            if x.rollno == rollnum:
                x.details()
            else:
                print("roll number not found")

    if command == "import to csv":
        for x in students:
            dictionary = x.importcsv(dictionary)

    if command == "exit":
        condition = False

print("end of program")
