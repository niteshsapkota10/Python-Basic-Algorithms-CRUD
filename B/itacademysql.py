import sqlite3

conn = sqlite3.connect("academy.sqlite3")
cursor = conn.cursor()
conn.execute('''create table if not exists students 
         (ID INTEGER PRIMARY KEY   AUTOINCREMENT     NOT NULL,
         name           TEXT    NOT NULL,
         education        CHAR(50)    NOT NULL,
         balance         INT      NOT NULL,
         remaining         INT      NOT NULL,
         course        CHAR(50)    NOT NULL,
         completed      INT    NOT NULL
         );''')


class Course:
    def __init__(self, choice):
        self.choice = choice

    def enroll(self, course_choice):
        tuple1 = ("Web Development", "Networking ", "Java Programming ")
        name = input("Enter your Fullname : ")
        education = input("Enter your Education Level : ")
        print("Enter your payment option: 1.Totally or 2.Installment")
        pay_opt = int(input("Enter your Choice: "))
        if pay_opt == 1:
            payment = 20000
        elif pay_opt == 2:
            payment = 10000
        remaining = 20000-payment
        completed = 0
        insert_sql = """INSERT INTO students (name, education, balance, remaining, course, completed) 
                          VALUES (?, ?, ?, ?, ?, ?);"""
        cursor.execute(insert_sql, (name, education, payment,
                                    remaining, tuple1[course_choice-1], completed))
        conn.commit()
        print("Data Insertion SuccessFull ")

    @staticmethod
    def getInfo():
        print("\t\t Welcome to IT ACADEMY ")
        print("\n Choose the course Your are intrested in : ")
        print("1.Web Development ")
        print("2.Networking ")
        print("3 Java Programming ")
        print("4 See Students Information ")
        print("5.Update Information ")
        print("6.Delete Information ")
        print("7.Course Completed..")

    def takeChoice(self):
        if self.choice == 1:
            self.webDevelopment()
        elif self.choice == 2:
            self.networking()
        elif self.choice == 3:
            self.javaprogramming()
        elif self.choice == 4:
            self.seeInformation()
        elif self.choice == 5:
            self.updateInformation()
        elif self.choice == 6:
            self.deleteInfo()
        elif self.choice == 7:
            self.courseCompleted()
        else:
            print("Choose Correct Option ")

    def webDevelopment(self):
        print("\n This is Full Stack Web Development Course ..\n And You have to deposit Rs.20000 , either at a time or in 2 installments and after course completion you will get it back ")
        print(
            "Here You will learn about Web Architecture..and it goes in given order..")
        print("1.HTML,CSS,JS - 1 project ")
        print("2.Core Python -1 project")
        print("3.Flask WebFramework in Python - 1 project ")
        print("4.Django -1 project")
        print("You want to Enroll (Y/N) ? ")
        ch = input("Press Y to enroll ")
        if ch == 'Y':
            self.enroll(self.choice)

    def networking(self):
        print("\n This is Networking Course ..\n And You have to deposit Rs.20000 , either at a time or in 2 installments and after course completion you will get it back ")
        print(
            "Here You will learn about Basics of Networking..")
        print("1. OSI Model")
        print("2. Protocols ")
        print("3. Cisco Packet Tracer")
        print("4. Servers ")
        print("You want to Enroll (Y/N) ? ")
        ch = input("Press Y to enroll ")
        if ch == 'Y':
            self.enroll(self.choice)

    def javaprogramming(self):
        print("\n This is Java Programming Course ..\n And You have to deposit Rs.20000 , either at a time or in 2 installments and after course completion you will get it back ")
        print(
            "Here You will learn about Java Programming..and it goes in given order..")
        print("1. Basics ")
        print("2. OOP in JAVA ")
        print("3. JDBC ")
        print("4. SWING -1 project")
        print("You want to Enroll (Y/N) ? ")
        ch = input("Press Y to enroll")
        if ch == 'Y':
            self.enroll(self.choice)

    def seeInformation(self):
        cursor = conn.execute(
            "SELECT id,name, education, balance, remaining, course, completed from students")
        print(
            f'ID \t Name \t\t Education \t\t Balance \t\t Remaining \t\t Course \t\t Completed')
        for row in cursor:
            print(
                f'{row[0]} \t {row[1]}  {row[2]} \t\t\t {row[3]} \t\t {row[4]} \t\t {row[5]} \t\t {row[6]}')

    def updateInformation(self):
        name = input("Which Student Details is to be updated? Enter Name..")
        new_education = input("New Education Level: ")
        select_sql = """Select balance from students where name=?"""
        row = cursor.execute(select_sql, (name,))
        my_balance = row.fetchone()
        try:
            if my_balance[0] == 10000:
                print("Do You Want to Pay Installment (Y/N) ??")
                your_choice = input("Enter Your Choice..")
                if your_choice == 'Y':
                    new_sql = """UPDATE students SET education=?,balance='20000',remaining='0' WHERE name=?"""
                    conn.execute(new_sql, (new_education, name,))
                    conn.commit()
                    print("SuccessFully Updated Thank You ")
                elif your_choice == 'N':
                    new_sql = """UPDATE students SET education=? WHERE name=?"""
                    conn.execute(new_sql, (new_education, name,))
                    conn.commit()
                    print("SuccessFully Updated Thank You ")
                else:
                    print("GETTING OUT OF IT...!!")
            else:
                new_sql = """UPDATE students SET education=? WHERE name=?"""
                conn.execute(new_sql, (new_education, name,))
                conn.commit()
                print("SuccessFully Updated Thank You ")
        except TypeError:
            print("Sorry No Student Found ")

    def deleteInfo(self):
        name = input("Which Student Details is to be Deleted ? Enter Name..")
        your_choice = input("Are you Sure Want to Delete (Y/N) ??")
        if your_choice == 'Y':
            del_sql = """DELETE from students where name=?"""
            conn.execute(del_sql, (name,))
            conn.commit()
            print(name, " Detail Successfully Deleted ")

    def courseCompleted(self):
        name = input("Enter Name..")
        select_sql = """Select balance from students where name=?"""
        row = cursor.execute(select_sql, (name,))
        my_balance = row.fetchone()
        try:
            if my_balance[0] == 10000:
                print("Sorry You cannot Complete Course Wihout full Balance ...!!")
            else:
                new_sql = """UPDATE students SET balance='0',completed='1' WHERE name=?"""
                conn.execute(new_sql, (name,))
                conn.commit()
                print(
                    "Congratulations for your Course Completion ..!\nWe are Happy for You..\n Hope You have a great Future..")
                print("Your Rs.20000 is returned...")

        except TypeError:
            print("Sorry Student Not Found")


Course.getInfo()
ch = int(input("Which Course Are You Intrested In:"))
c1 = Course(ch)
c1.takeChoice()
