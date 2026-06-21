from django.db import models

import uuid

# Create your models here.

class BookingmodelName(models.Model):
    booking_id = models.UUIDField(default=uuid=uuid4,unique=True,editable=False)
    

