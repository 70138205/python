from django.urls import path
from firstapp import views
urlpatterns=[
    # path('jan/',views.index),
    # path('feb/',views.index1),
    path('challenge/<str:month>/', views.index),

]
