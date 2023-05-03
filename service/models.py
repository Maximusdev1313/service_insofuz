from django.db import models

# Create your models here.


class Worker(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    fname = models.CharField(max_length=50)
    tel_number = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=20)
    worker_tip = models.CharField(max_length=20)
    today_money = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.fname


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    worker_id = models.ForeignKey(
        'Worker', on_delete=models.CASCADE, related_name='user_for_worker')

    def __str__(self):
        return self.fname


class WorkerReport(models.Model):
    date = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    worker_id = models.ForeignKey(
        'Worker', on_delete=models.CASCADE, related_name='report_worker')

    def __str__(self):
        return self.date


class ReturnForUser(models.Model):
    bar_code = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    img_link = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='order_for_user')

    def __str__(self):
        return self.name
