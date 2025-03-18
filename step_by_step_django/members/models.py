from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200)
  phone = models.IntegerField(null = True)
  joined_date = models.DateField(null=True)

### Below Models are ones For Django documentation.

# class Question(models.Model):
#   question_text = models.CharField(max_length=200)
#   pub_date = models.DateTimeField("date published")

# class Choice(models.Model):
#   question = models.ForeignKey(Question, on_delete = models.CASCADE)
#   choice_text = models.CharField(max_length=200)
#   votes = models.IntegerField(max_length=200)