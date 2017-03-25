#Declaration de la classe "facade"
class Facade:
	def __init__(self):
		name = "facade"

	def newStudent(self, firstname, lastname, age, avg):
		return Student(firstname, lastname, age, avg)

	def getStudent(self, firstname):
		for student in Student.getStudents():
			if (student.getFirstname() == firstname):
				return student
		print("no student with this firstname found")
		return null

	def newTeacher(self, firstname, lastname, age, subject):
		return Teacher(firstname, lastname, age, subject)

	def getTeacher(self, firstname):
		for teacher in Teacher.getTeachers():
			if (teacher.getFirstname() == firstname):
				return teacher
		print("no teacher with this firstname found")
		return null

	def newGroup(self, name, teacher, students):
		return StudentGroup(name, teacher, students)

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

	def printGroups(self):
		string = ""
		for group in StudentGroup.getGroups():
			string += group.toString()

		return string





	

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
		return "Student fn: "+ self.getFirstname() + " student ln: "+ self.getLastname() + " Student age: "+ self.getAge()

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
		return "Teacher fn: "+ self.getFirstname() + " Teacher ln: "+ self.getLastname() + " Teacher age: "+ self.getAge()

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

		return "Group name:"+ self.name +"\n Group students: "+ studentString + "\n Teacher: "+ self.teacher.getFirstname() +"\n" 


if __name__ == "__main__":
	
	#Testing without facade element
	'''
	combefis = Teacher("Sebastien", "Combefis", "30", "Informatique")
	lorge = Teacher("Andre", "Lorge", "45", "Informatique")
	yannick = Student("Yannick", "Berckmans", "23", "15")
	charles = Student("Charles","Vandevoorde", "23", "18")
	antoine = Student("Antoine", "VDM", "23", "15")
	gaetano = Student("Gaetano", "Giordano", "24", "13")
	group1 = StudentGroup("BestGroupEver", combefis, [yannick, charles])
	group2 = StudentGroup("AnotherGroup", lorge, [antoine, gaetano])

	print("Printing!")
	print("-----------------------------------------------")
	print("Every Teachers: ")
	for teacher in Teacher.teachers:
		print(teacher.toString())

	print("-----------------------------------------------")
	print("Every Students: ")
	for student in Student.students:
		print(student.toString())

	print("-----------------------------------------------")
	print("Every Groups: ")
	for group in StudentGroup.groups:
		print(group.toString())

	'''

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

	print("Finding those students and teachers and creating a group")
	#name, teacher, students
	facade.newGroup("BestGroupEver", facade.getTeacher("Sebastien"), [facade.getStudent("Yannick"),facade.getStudent("Charles")])
	facade.newGroup("AnotherGroup", facade.getTeacher("Andre"), [facade.getStudent("Gaetano"),facade.getStudent("Antoine")])
	print(facade.printGroups())
	
