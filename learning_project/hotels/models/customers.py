from django.contrib.auth.models import User
from django.db import models

class Customer(User):
    avatar = models.ImageField()
    phone = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=12)
    pan_card = models.CharField(max_length=10)
    address = models.TextField()
    signed_up_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def to_json(self, detailed=False):
        doc = {
            "name": self.get_full_name(),
            "avatar": self.avatar,
            "phone": self.phone,
            "email": self.email,
            "signed_up_on": str(self.signed_up_on) if self.signed_up_on else None
        }
        if detailed:
            doc["aadhar"] = self.aadhar
            doc["pan_card"] = self.pan_card
            doc["address"] = self.address
        return doc
