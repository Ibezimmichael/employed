from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employee_department', null=True)

    def __str__(self):
        return self.name