from django.db import models

# Create your models here.

# メンバー管理クラス
class Member(models.Model):
    name = models.CharField(max_length=30)

# KeepとProblem用クラス
class ProblemKeep(models.Model):
    start_date = models.DateField()
    title = models.CharField(max_length=200)
    presenter = models.ForeignKey(Member, related_name='pk_presenter')
    contributer = models.ManyToManyField(Member, related_name='pk_contributer', blank=True)

# Tryの親要素
class TryParent(models.Model):
    target_kp = models.ForeignKey(ProblemKeep)
    try_idea = models.CharField(max_length=200)

# 実際に行ったTry
class TryAction(models.Model):
    try_action = models.CharField(max_length=200)
    actor = models.ManyToManyField(Member, blank=True)
    canceled_date = models.DateField(blank=True, null=True)
    canceled_reason = models.CharField(max_length=200, blank=True, null=True)
    try_idea = models.ForeignKey(TryParent, blank=True, null=True)

# Tryに対するコメント  
class Comment(models.Model):
    comment = models.CharField(max_length=500, blank=True, null=True)
    belong = models.ForeignKey(TryAction, blank=True, null=True)

# レビュークラス
class Review(models.Model):
    schedule = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=200, blank=True, null=True)
    meeting = models.ForeignKey(TryAction, blank=True, null=True)

# Tryに対する意見
class OpinionForTry(models.Model):
    opinion = models.TextField()
    action = models.ForeignKey(TryAction, blank=True, null=True)

# ミーティングクラス
class Meeting(models.Model):
    date = models.DateField()
    author = models.ForeignKey(Member, related_name='mtg_auther', blank=True, null=True)
    presenter = models.ForeignKey(Member, related_name='mtg_presenter', blank=True, null=True)
    reporter = models.ForeignKey(Member, related_name='mtg_reporter', blank=True, null=True)
    report = models.CharField(max_length=1000, blank=True, null=True)

