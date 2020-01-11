from django.urls import path
from django.views.generic import TemplateView
from .views import search_view, page_view, page_download_view


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('search/', search_view, name='search'),
    path('page/', page_view, name='page'),
    path('download/', page_download_view, name='download')
]