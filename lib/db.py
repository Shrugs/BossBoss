from info import *
from peewee import *
import datetime

db = MySQLDatabase('OfCourse', user='OfCourse', passwd='OfCourseOfCourse')

class OCModel(Model):

    class Meta:
        database = db

class Department(OCModel):
    DeptID = PrimaryKeyField(primary_key=True, auto_increment=True)
    Dept = CharField(100)

class Subject(OCModel):
    SubjectID = CharField(primary_key=True)
    Subject = CharField(150)

class College(OCModel):
    CollegeID = PrimaryKeyField(primary_key=True)
    College = CharField(100)

class Course(OCModel):
    CourseID = PrimaryKeyField(primary_key=True)
    Course = CharField(100)
    College = ForeignKeyField(College, related_name='Courses')
    CourseCode = CharField(20)
    CreditsMax = IntegerField()
    CreditsMin = IntegerField()
    Description = TextField()
    Dept = ForeignKeyField(Department, related_name='Courses')
    Subject = ForeignKeyField(Subject, related_name='Courses')
    TSAdded = DateTimeField(default=datetime.datetime.now)

class Teacher(OCModel):
    TeacherID = PrimaryKeyField(primary_key=True, auto_increment=True)
    Name = CharField()
    Website = TextField()
    College = ForeignKeyField(College, related_name='Teachers')

class Class(OCModel):
    ClassID = PrimaryKeyField(primary_key=True, auto_increment=True)
    ClassCode = CharField(3) #001, 002, H01, etc
    Course = ForeignKeyField(Course, related_name='Classes')
    Days = CharField(3)
    TimeStart = TimeField()
    TimeEnd = TimeField()
    Teacher = ForeignKeyField(Teacher, related_name='Classes')
    TSAdded = DateTimeField(default=datetime.datetime.now)
