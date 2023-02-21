from django.urls import path
from .views import item_detail, buy_item
from django.views.generic import TemplateView

urlpatterns = [
    path('item/<int:id>/', item_detail, name='item_detail'),
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('cancel/', TemplateView.as_view(template_name='cancel.html'), name='cancel'),
]
