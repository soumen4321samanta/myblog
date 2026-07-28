from django.urls import path

from blog import api_views
from . import views


app_name='blog' #namespace ----- template e blog:post-list likhte parbo

urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('post/<int:pk>/',views.post_detail,name='post-detail'),  #/post/1/
    path('post/create/',views.post_create,name='post-create'),     #/post/create/
    path('post/<int:pk>/edit/',views.post_edit,name='post-edit'),  #/post/1/edit/
    path('post/<int:pk>/delete/',views.post_delete,name='post-delete'),  #/post/1/delete/



    # API URLs (নতুন)
    path('api/posts/', api_views.post_list_api, name='api-post-list'),
    path('api/posts/<int:pk>/', api_views.post_detail_api, name='api-post-detail'),

]
