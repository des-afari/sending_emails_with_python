from django.db import models

# Create your models here.
class Recipient(models.Model):
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email 

    def get_emails(self):
        return self.email

