from django.db import models
from django.utils import timezone
from django.urls import reverse # 新しく追加


class Staff(models.Model):
    """ スタッフ """
    family_name = models.CharField(
        verbose_name="姓（漢字）",
        max_length=50
    )
    given_name = models.CharField(
        verbose_name='名（漢字）',
        max_length=50
    )
    family_kana = models.CharField(
        verbose_name = '姓（カタカナ）',
        max_length = 50,
    )
    given_kana = models.CharField(
        verbose_name = '名（カタカナ）',
        max_length = 50,
    )  
    department = models.CharField(
        verbose_name="所属部署",
        max_length=225
    )

    def __str__(self):
        return f'{self.family_name} {self.given_name}'

    def name(self):
        """ 氏名 """
        return f'{self.family_name} {self.given_name}'

    class Meta:
        verbose_name = 'スタッフ'
        verbose_name_plural = 'スタッフ'


class BodyTemp(models.Model):
    """ 体温 """
    name = models.ForeignKey(
        Staff,
        verbose_name='名前',
        on_delete=models.PROTECT,
    )
    temp = models.DecimalField(
        verbose_name='体温',
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        verbose_name='検温日',
        default=timezone.now,
    )
    revised_at = models.DateField(
        verbose_name='更新日',
        auto_now=True,
    )

    def __str__(self):
        return f'{self.created_at} {self.name}'

    class Meta:
        verbose_name = '体温'
        verbose_name_plural = '体温'

    def get_absolute_url(self):
        return reverse('body_temp:day',
                       args=[self.created_at.year, self.created_at.month, self.created_at.day])