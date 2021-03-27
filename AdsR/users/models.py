from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

# def validate_number(number):
#     if len(str(number)) == 7:
#         return number
#     else:
#         raise ValidationError("Telefon raqam 7 raqamdan iborat bulishi kerak!")   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    bio = models.TextField(max_length=200)
    instagram = models.CharField(max_length=50 ,blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
     
    # phonenumber_code = models.CharField(max_length=2, choices=code_choices, default=91)
    # phonenumber = models.IntegerField(validators=[validate_number], default=1234567)

    def __str__(self):
        return "{}-profile".format(self.user.username)
    
 
