from django.conf.urls import url

from images import views

urlpatterns = [
    url(r'^images/?$', views.ImageListView.as_view(), name='image_list'),
    url(r'^image/(?P<uuid>[a-zA-Z0-9]+)', views.ImageView.as_view(), name='image'),
    url(r'^like/', views.LikeView.as_view(), name='like'),
]