from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    body = models.TextField(null=True)
    author = models.ForeignKey("Author", related_name="articles", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title