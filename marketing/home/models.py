from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    company_name = models.CharField(max_length=120)
    details = models.TextField()

    
    def __str__(self):
        return self.first_name + self.last_name