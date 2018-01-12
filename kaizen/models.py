from django.db import models

# Create your models here.


class Member(models.Model):
    #id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

class ProblemKeep(models.Model):
    #id = models.CharField(unique=True, max_length=5)
    start_date = models.DateField()
    title = models.CharField(max_length=200)
    presenter = models.ForeignKey(Member, related_name='pk_presenter')#IntegerField()
    contributer = models.ManyToManyField(Member, related_name='pk_contributer', blank=True)#(blank=True, null=True)

class TryParent(models.Model):
    #id = models.CharField(unique=True, max_length=5)
    target_kp = models.ForeignKey(ProblemKeep)
    try_idea = models.CharField(max_length=200)

class TryAction(models.Model):
    #id = models.CharField(unique=True, max_length=5)
    try_action = models.CharField(max_length=200)
    actor = models.ManyToManyField(Member, blank=True)
    canceled_date = models.DateField(blank=True, null=True)
    canceled_reason = models.CharField(max_length=200, blank=True, null=True)
    try_idea = models.ForeignKey(TryParent, blank=True, null=True)

class Comment(models.Model):
    #id = models.IntegerField()
    comment = models.CharField(max_length=500, blank=True, null=True)
    belong = models.ForeignKey(TryAction, blank=True, null=True)



class Review(models.Model):
    #id = models.IntegerField(unique=True)
    schedule = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=200, blank=True, null=True)
    meeting = models.ForeignKey(TryAction, blank=True, null=True)


class OpinionForTry(models.Model):
    #id = models.IntegerField(unique=True)
    opinion = models.TextField()
    action = models.ForeignKey(TryAction, blank=True, null=True)


class Meeting(models.Model):
    #id = models.CharField(unique=True, max_length=5)
    date = models.DateField()
    author = models.ForeignKey(Member, related_name='mtg_auther', blank=True, null=True)
    presenter = models.ForeignKey(Member, related_name='mtg_presenter', blank=True, null=True)
    reporter = models.ForeignKey(Member, related_name='mtg_reporter', blank=True, null=True)
    report = models.CharField(max_length=1000, blank=True, null=True)

