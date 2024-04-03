from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    

class DailyDiary(models.Model):
    # user = models.ForeignKey(User, related_name="diary", on_delete=models.CASCADE) # CASCADE : userが消されたら、dailydiaryも一緒に消える
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    created_date = models.DateField(auto_now=True) # auto_now : 一度きり, auto_now : 更新された日時をその度に記録