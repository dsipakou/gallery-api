from django.conf.urls import url

from images import views

urlpatterns = [
    url(r'^images/?$', views.ImageListView.as_view({'get': 'list'}), name='image_list'),
    url(r'^images/(?P<date>[0-9-]+)/?$', views.ImageListView.as_view({'get': 'date_list'}), name='image_archive_list'),
    url(r'^hot/?$', views.HotImageView.as_view(), name='hot_image'),
    url(r'^image/(?P<uuid>[a-zA-Z0-9]+)/?$', views.ImageView.as_view(), name='image'),
    url(r'^like/(?P<uuid>[a-zA-Z0-9]+)/?$', views.LikeView.as_view({'get': 'get'}), name='get_like'),
    url(r'^like/?$', views.LikeView.as_view({'post': 'post', 'delete': 'delete'}), name='like'),

]