# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone



# class Post(models.Model):
# # 	author = models.ForeignKey(User, on_delete=models.CASCADE)
# # 	def __str__(self):
# # 		return self.author


# # class House(models.Model):
# # 	owner = models.CharField(max_length=250)
# # 	house_title = models.CharField(max_length=500)
# # 	contact = models.CharField(max_length=100)
# # 	address = models.CharField(max_length=1000)
# # 	image = models.ImageField(default='default.jpg', upload_to='Apartment_pics')
# # 	def __str__(self):
# # 		return self.house_title +':'+ self.owner

# # class Appart(models.Model):
# # 	house = models.ForeignKey(House, on_delete=models.CASCADE)
# # 	ap_type = models.CharField(max_length=10)
# # 	ap_name = models.CharField(max_length=250)
		
# # 	def __str__(self):
# # 		return self.ap_name


from django.db import models


class Post(models.Model):
    owner = models.CharField(verbose_name='blog', max_length=128)


