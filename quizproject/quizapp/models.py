from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    user = models.ForeignKey(User, default=id, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=_("New Quiz"),
        verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Question(models.Model):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=_("Question"),verbose_name=_("Title"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))
    user = models.ForeignKey(User, default=id, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    

class Answer(models.Model):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    user = models.ForeignKey(User, default=id, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Player(models.Model):

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")
        ordering = ['id']
    
    user = models.ForeignKey(User, default=id, on_delete=models.DO_NOTHING)
    quiz = models.ForeignKey(Quizzes, on_delete=models.DO_NOTHING)
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

