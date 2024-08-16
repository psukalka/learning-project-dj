from django.db import models
from django.utils import timezone

def upload_userprofile_avatar(instance, filename):
    return 'avatars/%s.%s' % (str(timezone.now().second), filename.split('.')[-1])

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    avatar = models.ImageField(upload_to=upload_userprofile_avatar, null=True, blank=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    signed_up_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": f"{self.first_name} {self.last_name}",
            "phone": self.phone,
            "email": self.email,
            "signed_up_on": str(self.signed_up_on)
        }