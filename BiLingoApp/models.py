from distutils.command.upload import upload
from email.policy import default
from enum import auto
from math import fabs
from multiprocessing.connection import answer_challenge
from unicodedata import category
import uuid
import random
# User model 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,null=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

# quuiz
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True , default=uuid.uuid4)
    category_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract= True


class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class Question(BaseModel):
    category = models.ForeignKey(Category ,related_name='category' , on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer': answer_obj.answer,
                'is_correct':answer_obj.is_correct,
            })

        return data


class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

