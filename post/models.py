from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError

FILTERED_WORDS = ["TEST", "TTTT"]
def validate_filter_words(content):
    if any(word in content.upper() for word in FILTERED_WORDS):
        raise ValidationError('Contains restriced words!')

class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    content = models.CharField(max_length=140, validators=[validate_filter_words])
    created_on = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.content[0:20])