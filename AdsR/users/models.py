from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

def validate_number(number):
    if len(str(number)) == 7:
        return number
    else:
        raise ValidationError("Telefon raqam 7 raqamdan iborat bulishi kerak!")   

class Profile(models.Model):
    code_choices = (
        ('88',88),
        ('90',90),
        ('91',91), 
        ('93',93),
        ('94',94),
        ('95',95),
        ('98',98),
        ('99',99)
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber_code = models.CharField(max_length=2, choices=code_choices, default=91)
    phonenumber = models.IntegerField(validators=[validate_number], default=1234567)

    def __str__(self):
        return "{}-profile".format(self.user.username)
    
 
