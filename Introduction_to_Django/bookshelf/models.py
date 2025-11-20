from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
    
#one to many relationship example
#Create a model representing a company with departments and employees, using ForeignKey relationships
class Company(models.Model):
    name = models.CharField(max_length=200)
     
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='departments')
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    on_contract = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    def __str__(self):
        return self.name
 
 #one to one relationship example   
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    
class Description(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()
    
#many to many relationship example
class Students(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    
class Courses(models.Model):
    student = models.ManyToManyField(Students, related_name='courses')
    
# optimizing queries with pre-fetching ==> django will perform a separate query to fetch all related department instances, reducing the number of DB queries and improving performance
employees = Employee.objects.prefetch_related('department')