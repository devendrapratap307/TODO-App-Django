
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title  status current_date  user  priority


class TODO(models.Model):
    status_choices = [
    ('D', 'DONE'),
    ('P', 'PENDING'),
    ]
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]
    title = models.CharField(max_length=60)
    status = models.CharField(max_length=2 , choices=status_choices)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 , choices=priority_choices)