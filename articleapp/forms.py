

from django.db.models import fields
from articleapp.models import Article
from django.db.models.base import Model
from django.forms import ModelForm
from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content ']