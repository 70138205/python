from django.urls import path
from second_app import views
urlpatterns=[
    path('jan/',views.index),
    path('feb/',views.index1),
    path('mar/',views.index2),
    path('apr/',views.index3),
    path('may/',views.index4),
    path('june/',views.index5),
    path('july/',views.index6),
    path('aug/',views.index7),
    path('sep/',views.index8),
    path('oct/',views.index9),
    path('nov/',views.index10),
    path('dec/',views.index11),

]