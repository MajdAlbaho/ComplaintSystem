from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

CATEGORY_CHOICES = [
    ('academic','Academic'),
    ('mess', 'Mess'),
    ('sports', 'Sports'),
    ('student_affairs', 'Student affairs'),
    ('hostel', 'Hostel'),
    ('security', 'Security'),
    ('guest_house', 'Guest House'),
    ('library', 'Library'),
    ('other', 'Other'),
]
class Complaint(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    is_anonymous= models.BooleanField(default=False)
    photo = models.ImageField(null=True, default=None,)
    
    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('comlpeted', 'Completed'),
        ('closed', 'Closed')
    ]
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='reported',
    )
    category = models.CharField(
        max_length=18,
        choices=CATEGORY_CHOICES,
        default='other',
    )
    created_date = models.DateTimeField(default=timezone.now)

    def register(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    head_of = models.CharField(
        max_length=18,
        choices = CATEGORY_CHOICES,
        default = ''
    )
    id = models.AutoField(primary_key=True)


class Remark(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateField(default=timezone.now)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
