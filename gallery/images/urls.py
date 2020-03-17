from django.conf.urls import url

from images import views

urlpatterns = [
    url(r'^images/?$', views.ImageListView.as_view(), name='image_list')
]