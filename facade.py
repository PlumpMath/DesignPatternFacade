import sys

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#Declaration de la classe "facade"
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


class Facade:
	def __init__(self):
		name = "facade"

	def newStudent(self, firstname, lastname, age, avg):
		Student(firstname, lastname, age, avg)

	def getStudent(self, firstname):
		for student in Student.getStudents():
			if (student.getFirstname() == firstname):
				return student
		print("no student with this firstname found")
		return null

	def newTeacher(self, firstname, lastname, age, subject):
		Teacher(firstname, lastname, age, subject)

	def getTeacher(self, firstname):
		for teacher in Teacher.getTeachers():
			if (teacher.getFirstname() == firstname):
				return teacher
		print("no teacher with this firstname found")
		return null

	def newGroup(self, name, teacher, students):
		StudentGroup(name, teacher, students)

	def getGroup(self, groupname):
		for group in StudentGroup.getGroups():
			if (group.getName() == groupname):
				return group
		print("no group with this name found")
		return null		

	def getStudentFirstname(self, student):
		return student.getFirstname()

	def getStudentLastname(self, student):
		return student.getLastname()

	def getStudentAge(self, student):
		return student.getAge()

	def getStudentAvg(self, student):
		return student.getAvg()

	def getTeacherFirstname(self, teacher):
		return teacher.getFirstname()

	def getTeacherLastname(self, teacher):
		return teacher.getLastname()

	def getTeacherAge(self, teacher):
		return teacher.getAge()

	def getTeacherSubject(self, teacher):
		return teacher.getSubject()

	def getGroupTeacher(self, group):
		return group.getTeacher()

	def getGroupStudents(self, group):
		return group.getStudents()

	def printStudents(self):
		string = "----------------------\n"
		for student in Student.getStudents():
			string += student.toString()

		return string

	def printTeachers(self):
		string = "----------------------\n"
		for teacher in Teacher.getTeachers():
			string += teacher.toString()

		return string

	def printGroups(self):
		string = "----------------------\n"
		for group in StudentGroup.getGroups():
			string += group.toString()

		return string


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#Declaration des classes du programme
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


#Declaration de la classe abstraite "Personne"
class Person:
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age

#Declaration de la classe "Student"
class Student(Person):

	#Attribut statique listant l'ensemble des students
	students = []
	def __init__(self, firstname, lastname, age, avg):
		Person.__init__(self, firstname, lastname, age)
		self.avg = avg
		Student.students.append(self)

	def getFirstname(self):
		return self.firstname

	def getLastname(self):
		return self.lastname

	def getAge(self):
		return self.age

	def getAvg(self):
		return self.avg

	def toString(self):
		return "Student firstname: "+ self.getFirstname() + "\nstudent lastname: "+ self.getLastname() + "\nStudent age: "+ str(self.getAge()) + "\n ----------------------\n"

	@staticmethod
	def getStudents():
		return Student.students

#Declaration de la classe "Teacher"
class Teacher(Person):

	#Attribut statique listant l'ensemble des teachers
	teachers = []
	def __init__(self, firstname, lastname, age, subject):
		Person.__init__(self, firstname, lastname, age)
		self.subject = subject
		Teacher.teachers.append(self)
	
	def getFirstname(self):
		return self.firstname

	def getLastname(self):
		return self.lastname

	def getAge(self):
		return self.age

	def getSubject (self):
		return self.subject

	def toString(self):
		return "Teacher firstname: "+ self.getFirstname() + "\nTeacher lastname: "+ self.getLastname() + "\nTeacher age: "+ str(self.getAge()) + "\n ----------------------\n"

	@staticmethod
	def getTeachers():
		return Teacher.teachers

#Declaration de la classe "StudentGroup"
class StudentGroup:
	
	groups = []
	def __init__(self, name, teacher, students):
		self.name = name
		self.teacher = teacher
		self.students = students
		StudentGroup.groups.append(self)

	@staticmethod
	def getGroups():
		return StudentGroup.groups

	def getName (self):
		return self.name

	def getTeacher(self):
		return self.teacher

	def getStudent(self):
		return self.student

	def toString(self):
		studentString = ""
		for student in self.students:
			studentString += student.getFirstname() + ", "

		return "Group name:"+ self.name +"\n Group students: "+ studentString + "\n Teacher: "+ self.teacher.getFirstname() +"\n----------------------\n" 


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#Declaration de la fonction "BASH"
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


def bash(string, facade):
	#Splitting the string in param
	splitted = string.split()

	#Different cases
	#Exit
	if (splitted[0] == "exit" or splitted[0] == "end"):
		sys.exit()

	#Cmd
	if (splitted[0] == "cmd"):
		print("--------------------------------------------")
		print("List of all commands available")
		print("-Create a student: newS firstname lastname age avg")
		print("-Create a teacher: newT firstname lastname age subject")
		print("-Create a group (note the - between students): newG groupName teacherName student1-student2-student3")
		print("-printS to get all the students")
		print("-printT to get all the teachers")
		print("-printG to get all the groups")

		print("--------------------------------------------")
		return

	#Create a new student
	if(splitted[0] == "newS"):
		#First param = firstname
		#Second param = lastname
		#Third param = age
		#Fourth param = avg
		try:
			facade.newStudent(splitted[1], splitted[2], splitted[3], splitted[4])
			print("Created a new student with the firstname %s" %(splitted[1]))
		except:
			print("To create a new student, you need this syntax: newS firstname lastname age avg")

		return

	#Create a new teacher
	if(splitted[0] == "newT"):
		#First param = firstname
		#Second param = lastname
		#Third param = age
		#Fourth param = subject
		try:
			facade.newTeacher(splitted[1], splitted[2], splitted[3], splitted[4])
			print("Created a new teacher with the firstname %s" %(splitted[1]))
		except:
			print("To create a new teacher, you need this syntax: newT firstname lastname age subject")

		return

	#Create a new group
	if(splitted[0] == "newG"):
		#First param = group name
		#Second param = teacher name
		#Third param = array of students
		
		#Splitting the third parameters to get the different students name
		studentsString=splitted[3].split('-')
		studentsObject = []

		#Finding all the objects "students" with the name given
		for student in studentsString:
			try:
				studentsObject.append(facade.getStudent(student))
			except:
				print("Can't find the student with the name %s" % (student))

		try:
			facade.newGroup(splitted[1], facade.getTeacher(splitted[2]), studentsObject)
			print("Created new group with the name %s" %(splitted[1])) 
		except:
			print("To create a new group, you need this syntax: newG groupName teacherFirstname student1-student2-student3")

		return
	if(splitted[0] == "printS"):
		print(facade.printStudents())
		return

	if(splitted[0] == "printT"):
		print(facade.printTeachers())
		return

	if(splitted[0] == "printG"):
		print(facade.printGroups())
		return

	print("No command found!")
	return

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#TESTS + main
#NOTICE THAT WE ONLY USE THE FACADE OBJECT!
#THIS IS THE PURPOSE OF THE DESIGN PATTERN!
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
if __name__ == "__main__":
	


	#Testing using only the facade Class
	print("Creating students and teachers with the Facade Class...")
	facade = Facade()
	#facade.newStudent("Sylvain","Alonso",23,14)
	facade.newStudent("Yannick","Berckmans", 23, 15)
	facade.newStudent("Charles","Vandevoorde",23,18)
	facade.newStudent("Antoine","VDM", 23,15)
	facade.newStudent("Gaetano","Giordano",24,13)
	facade.newTeacher("Sebastien","Combefis",30,"Informatique")
	facade.newTeacher("Andre","Lorge",45,"Informatique")

	print("Creating the two first groups for the exemple...\n")
	#name, teacher, students
	facade.newGroup("BestGroupEver", facade.getTeacher("Sebastien"), [facade.getStudent("Yannick"),facade.getStudent("Charles")])
	facade.newGroup("AnotherGroup", facade.getTeacher("Andre"), [facade.getStudent("Gaetano"),facade.getStudent("Antoine")])
	print(facade.printGroups())
	while True:
		print("waiting for input (type cmd to get all the commands available)... ")
		vinput = raw_input(">>>")

		bash(vinput,facade)	


	
	
