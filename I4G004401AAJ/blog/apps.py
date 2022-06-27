from msilib.schema import ListView
import django
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

# class PostListView(ListView):
