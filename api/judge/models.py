from django.db import models
from django.contrib.auth import get_user_model


class Judge(models.Model):
    name = models.CharField(max_length=500)
    user_endpoint = models.CharField(max_length=500)


class ProblemCategory(models.Model):
    name = models.CharField(max_lenght=50)


class Problem(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    category = models.ForeignKey(ProblemCategory, on_delete=models.PROTECT)
    link = models.CharField(max_length=500)


class SubmissionAnswer(models.Model):
    name = models.CharField(max_length=500)
    solved = models.BooleanField()


class Submission(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    answer = models.OneToOneField(SubmissionAnswer, on_delete=models.PROTECT)
