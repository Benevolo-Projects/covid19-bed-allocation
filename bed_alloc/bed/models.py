from django.db import models
import glob, os
from django.db.models import F


def path_and_rename(instance, filename):
    name1 = str(len(glob.glob('../pdf/*')))
    print(name1)
    return os.path.join(name1 + ".pdf")


class Register(models.Model):
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    email = models.EmailField()
    mobile = models.IntegerField()
    age = models.IntegerField()
    ct = models.PositiveIntegerField()
    oxy = models.PositiveIntegerField()
    oc = models.PositiveIntegerField(default=135)
    ct_pdf = models.FileField(upload_to=path_and_rename, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.oc = self.ct + self.oxy
        super(Register, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname + ' ' + self.lname
