from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Todolist(models.Model):
    description = models.CharField(max_length=20, default='new', choices=STATUS_CHOICES, verbose_name='Описание')
    status = models.CharField(max_length=200, null=False, blank=False, verbose_name='Статус')
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Время создания')


    def __str__(self):
        return f"{self.pk}. {self.status}"

    class Meta:
        db_table = 'lists'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'