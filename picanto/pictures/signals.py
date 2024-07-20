from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import Customer



def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			name=instance.username,
			email=instance.email
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)


#	//////////////////////////////////////////////////////////
# @receiver(post_save,sender = User)
# def create_user_porfile(sender,instance,created,**kwargs) :
# 	if created :
# 		Customer.objects.create(user=instance)

# @receiver(post_save,sender = User)
# def save_user_profile(sender,instance,**kwargs) :
# 	instance.Customer.save()


# # 	instance.Customer.save()
#	//////////////////////////////////////////////////////////


