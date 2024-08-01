from django.urls import path
from .import views

urlpatterns = [
    path('postlist/',views.post_list,name='List'),
    path('add_blog/',views.add_blog,name='ADD'),
    path('single_blog/<int:id>/',views.single_blog,name='single')
]

