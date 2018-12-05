from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    birthday = models.DateTimeField()
    email = models.CharField(max_length=50, null=False)
    role_id = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.firstname, self.lastname, self.birthday, self.email, self.role_id)
