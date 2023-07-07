from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=255 , blank=False , null= False)
    body = models.TextField(max_length=1200 , blank=False , null= False)
    date = models.DateField()
    time = models.TimeField()
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ['complete']

