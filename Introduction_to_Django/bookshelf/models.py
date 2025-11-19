from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title

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