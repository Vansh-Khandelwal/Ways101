from django.db import models
from django.utils import timezone
from SignUp.models import User

# Create your models here.


# Way Model

class Way(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, default='')
    date = models.DateTimeField(timezone.now)

    upvotes = models.TextField(default="", null=True)
    downvotes = models.TextField(default = "", null=True)

    def _author_(self):
        return self.author

    def _content_(self):
        return self.content

    def _date_(self):
        return self.date

    def up(self):
        return self.upvotes.split(',')

    def down(self):
        return self.downvotes.split(',')

    def numberofupvotes(self):
        return len(self.up())-1

    def numberofdownvotes(self):
        return len(self.down())-1


# Comment Model

class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False)
    way = models.ForeignKey(Way, on_delete=models.CASCADE, null=False)

    date = models.DateTimeField(timezone.now)

    def _author_(self):
        return self.author

    def _comment_(self):
        return self.comment

    def _way_(self):
        return self.way

    def _date_(self):
        return self.date
