from django.urls import path
from .views import GetView

urlpatterns = [
    path('', GetView.as_view(), name='item-list'),
]
