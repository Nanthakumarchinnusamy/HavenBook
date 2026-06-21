from django.db import models

# Create your models here.

from formapp.models import Realtors

# Create your models here.
types=[
    ('BUY','buy'),
    ('SELL','sell'),
    ('RENTAL','rental'),
    ('LEASE','lease')   
]
cat=[
    ('1STORY','1story'),
    ('2STORY','2story'),
    ('3STORY','3story'),
    ('DUPLEX','duplex'),
    ('INDIVIDUAL','individual'),
    ('APARTMENT','apartment')
]

status=[
    ('soldout','SOLDOUT'),
    ('pending','PENDING')
]
class allproperties(models.Model):
    name=models.CharField(max_length=100) 
    property_type=models.CharField(choices=types)
    price=models.IntegerField()
    floors=models.CharField(max_length=100)
    category=models.CharField(choices=cat)
    age=models.IntegerField()
    area=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    no_of_rooms=models.IntegerField()
    no_of_bathrooms=models.IntegerField()
    balcony=models.BooleanField()
    attached_bathroom=models.BooleanField()
    owner_name=models.CharField(max_length=100)
    property_image=models.ImageField(upload_to='media/images/',blank=True,null=True)
    realtorname = models.ForeignKey(Realtors, related_name='realtorss', on_delete=models.CASCADE)
    verdict=models.CharField(max_length=100, choices=status)
    
    def __str__(self):
        return self.name
    
class Rooms(models.Model):
    rproperty = models.ForeignKey(allproperties,related_name='rallpropertics',on_delete=models.CASCADE)
    room_pics = models.ImageField(upload_to='media/rooms/',blank=True,null=True)

    # def __str__(self):
    #     return self.room_pics

class LivingArea(models.Model):
    lproperty = models.ForeignKey(allproperties,related_name='lallpropertics',on_delete=models.CASCADE)
    living_pics = models.ImageField(upload_to='media/livingarea/',blank=True,null=True)

    # def __str__(self):
    #     return self.lproperty

class Balcony(models.Model):
    baproperty = models.ForeignKey(allproperties,related_name='baallpropertics',on_delete=models.CASCADE)
    balcony_pics = models.ImageField(upload_to='media/balcony/',blank=True,null=True)

    # def __str__(self):
    #     return self.baproperty

class Bathroom(models.Model):
    brproperty = models.ForeignKey(allproperties,related_name='brallpropertics',on_delete=models.CASCADE)
    bathroom_pics = models.ImageField(upload_to='media/bathroom/',blank=True,null=True)

    # def __str__(self):
    #     return self.brproperty

class Kitchen(models.Model):
    kproperty = models.ForeignKey(allproperties,related_name='kallpropertics',on_delete=models.CASCADE)
    kitchen_pics = models.ImageField(upload_to='media/kitchen/',blank=True,null=True)

    # def __str__(self):
    #     return self.kproperty
