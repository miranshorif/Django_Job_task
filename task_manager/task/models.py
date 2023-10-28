from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=200)
    id              = models.AutoField(primary_key=True)
    image           = models.ImageField(default='default.jpg', upload_to='task/images')
    slug            = models.CharField(max_length=100,default=title)
    description     = models.TextField()
    due_date        = models.DateField()
    priority        = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    completed       = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    last_updated    = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Task,self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
    def __str__(self):
        return self.title