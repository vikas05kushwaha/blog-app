from audioop import maxpp
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
# from django_pandas.io import read_frame

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.CharField(max_length=122)
    # image=models.ImageField(upload_to='static/images/',null=True,default=None)
    date=models.DateField()
    def __str__(self):
        return self.name
    # def __str__(self):
        # return self.email

class Tag(models.Model):
    Title=models.CharField(max_length=122) 
    def __str__(self):
        return self.Title 

class Blog(models.Model):
    title=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    userid=models.CharField(max_length=122)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='static/images/',null=True,default=None)
    date=models.DateField(null=True,default=None)
    tags=models.ManyToManyField(Tag,verbose_name="My Tags", null=True,default=None)
    # contact=Contact.objects.get(id=idd)
    def __str__(self):
        return self.title

class cats(models.Model):
    class Meta:
        db_table="cats"
    name=models.CharField(max_length=200) 
    owner=models.CharField(max_length=200)
    def __str__(self):
        return self.owner

# class Staff(models.Model):
#     class Meta:
#         db_table="staff"
#     fullname=models.CharField(max_length=200) 
#     moblie=models.IntegerField()
#     def __str__(self):
#         return self.mobile
        


# class MyModel(models.Model):
#     full_name = models.CharField(max_length=25)
#     age = models.IntegerField()
#     department = models.CharField(max_length=3)
#     wage = models.FloatField()

# qs = MyModel.objects.all()
# df = read_frame(qs)

      