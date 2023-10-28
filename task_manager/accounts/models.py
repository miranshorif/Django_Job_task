from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    Gender=(
        ('Male','Male'),
        ('Female','Female'),
    )
    Category=(
        ('Student','Student'),
        ('Teacher','Teacher'),
    )
    Blood_Group=(
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O-','O-'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=3,choices=Blood_Group)
    gender = models.CharField(max_length=10,choices=Gender)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    nationality = models.CharField(max_length=90)
    religion = models.CharField(max_length=50)
    biodata = models.TextField()
    profession = models.CharField(max_length=50,choices=Category)
    image = models.ImageField(upload_to='accounts/images')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)