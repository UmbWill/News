from django.db import models

# Create your models here.
class News(models.Model):
    source_id = models.TextField(null=True)
    source_name = models.TextField()
    author= models.TextField( default='mistery_author', null=True)
    title= models.TextField()
    description= models.TextField(null=True)
    url= models.TextField()
    urlToImage= models.TextField(null=True)
    publishedAt= models.DateTimeField()
    content = models.TextField(null=True)

    def __str__(self):
        return self.title