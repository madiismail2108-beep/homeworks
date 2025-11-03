from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_add=False)
    description=models.CharField(max_length=1000)
    price=models.IntegerField()
    file=models.FileField(upload_to='book_file/')
    author=models.CharField(max_length=50)

    def __str__(self):
        return  f"{self.name} {self.author}"

# Create your models here.
