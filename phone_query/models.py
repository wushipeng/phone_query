from django.db import models

# Create your models here.


class PersonPhone(models.Model):
    """这是分机号信息"""
    name = models.CharField(max_length=32,null=False,verbose_name="员工姓名")
    pyjc = models.CharField(max_length=6,null=False,verbose_name="员工姓名简称")
    phone_number = models.IntegerField(null=False,verbose_name="分机号码")
    part = models.CharField(max_length=60,null=False, verbose_name="部门名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="本公司分机信息"


class RegionalPhone(models.Model):
    """各地区分机号码"""
    city_name = models.CharField(max_length=32,verbose_name="分公司所在城市名称")
    phone_number = models.CharField(max_length=16,verbose_name="电话号码")

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural="各地分机信息"
