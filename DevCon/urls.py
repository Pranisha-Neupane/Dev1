from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view,create_room,msg,join_room,view_room,myrooms

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create_room/',create_room,name='create_room'),
    path('join_room/<int:room_id>',join_room,name='join_room'),
    path('msg/<int:room_id>',msg,name='msg'),
    path('view_room/<int:room_id>',view_room,name='view_room'),
    path('myrooms',myrooms,name='myrooms')
]
