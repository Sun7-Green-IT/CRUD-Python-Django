from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    birthday = models.DateTimeField()
    role_id = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.firstname, self.lastname, self.email, self.birthday, self.role_id)
