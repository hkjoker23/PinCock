from django.db.models.base import Model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from django.urls import reverse, reverse_lazy


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DeleteView):
    Model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'