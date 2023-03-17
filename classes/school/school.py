import re

class School:
    count = 0
    __all__ = ["grade", "score", "remove_student", "from_list"]

    def __init__(self, fname, lname, *args):
        School.count += 1
        self.fn = fname
        self.ln = lname
        self.email = "{}.{}@edu.riga.lv".format(self.fn, self.ln)

    @property
    def fullname(self):
        return "{} {}".format(self.fn, self.ln)
    
    def grade(self):
        """sets self.grade and prints out a grade"""
        if self.score >= 90:
            self.grade = "A"
        elif self.score >= 80:
            self.grade = "B"
        elif self.score >= 70:
            self.grade = "C"
        elif self.score >= 60:
            self.grade = "D"
        else:
            self.grade = "F"
        return self.grade
        # ("{} has a {} (score : {})".format(self.fullname, self.grade, self.score))

    def score(self, answers):
        """calculates the score, by comparing a str of answers to an answer_key (self.score)"""
        answer_key = "ACBAACBBBC"
        right = 0
        max_score = len(answer_key)
        answers = answers[:10]
        for num, char in enumerate(answer_key):
            if char == answers[int(num)]:
                right += 1
        self.score = (right / max_score) * 100
        return self.score

    def remove_student(self):
        """removes a student from the database"""
        # read all the lines
        with open("classes/school/students.txt", "r") as f:
            lines = f.readlines()
        # write all lines except the one that is not needed
        with open("classes/school/students.txt", "w") as f:
            for line in lines:
                if self.fullname not in line:
                    f.write(line)

    def rank(self, others):
        """ranks students with their scores in order"""
        ranks = {
            self.fullname: self.score,
        }
        # appends the dict
        for students in others:
            ranks[students.fullname] = students.score
        # sorts by value
        return dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
        

    def set_email(self):
        """allows the user to input a new email"""
        
        self.email = re.search(
            "([\w]*[\.]?[\w]*@edu.riga.lv)", input("\n--Whats should be your new email? ")
            ).group()
        
        return self.email

    @classmethod
    def from_list(cls, lst):
        """makes a student from a list"""
        fname, lname, form, grade = lst
        return cls(fname, lname, form, grade)

    @classmethod
    def get_methods(cls):
        """prints all the methods in a class"""
        print(f"\nmethods: {cls.__all__}\n")

    def __str__(self):
        return f"-->{self.fullname}"

    def __repr__(self):
        return f"{self.__class__}"


class Student(School):
    __all__ = ["_print_major", School.__all__]

    def __init__(self, fname, lname, form, major: list = None):
        super().__init__(fname, lname)
        self.form = form
        if major is None:
            self.majors = []
        else:
            self.majors = major

        # maybe get it into the superclass??
        with open("/Users/ralfseduards/vscode-main/classes/school/students.txt", "r+") as f:
            lines = f.read()
            student_in = True if self.fullname in lines else False
            if not student_in:
                f.write("->" + self.fullname + str(self.majors) + "\n")

    def print_major(self):
        """prints the majors of a student"""
        print(self.fullname, "majors:")
        for major in self.majors:
            print("-->", major)


class Staff(School):
    def __init__(self, fname, lname, prof, tel):
        super().__init__(fname, lname)
        if len(tel) != 8:
            print(f"{self.fullname} phone number not Valid!")
            exit()

        self.prof = prof
        self.num = tel

    def pay(self):
        """sets the pay for a staff member"""
        if self.prof == "teacher":
            self.pay = 1000
        else:
            self.pay = 9
        return self.pay

    def set_num(self):
        """allows a staff member to change their phone number"""
        try:
            self.num = re.search(
                "^(\d{8})$", input("\nWhat is your phone num? ")
            ).group()
        except AttributeError:
            print("Number not valid!")
        return self.num


# vareetu regexes
def tests():
    ralph = School("Ralph", "Eduard", 12)
    list_bozo = ["John", "Doe", 11, 78]
    nobody = School.from_list(list_bozo)

    ralph.email()
    print(ralph.email)

    print("\nStudent count = {}".format(School.count))

    ralph.score("ACBSCBACAC")
    print(ralph.score)
    ralph.grade()


std1 = Student("First", "Boy", 11, ["Physics", "Math"])
std2 = Student("Second", "Boy", 11, ["Crafts", "Music"])
std3 = Student("Third", "Boy", 11, ["Art", "Chemisty"])
std4 = Student("Fourth", "Boy", 11, ["Python", "Latin"])

std1.score("ACBSCBABBC")
std2.score("ACBBCBACAC")
std3.score("ACBAABCCAC")
std4.score("ACBCCBACAC")

print(std1.rank([std2,std3,std4]))
Student.get_methods()

std4.print_major()

andzis = Staff("Math", "Andzis", "teacher", "12345678")

# print(andzis.email)
# andzis.set_email()
# print(andzis.email)
