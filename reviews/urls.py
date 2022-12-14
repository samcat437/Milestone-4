from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('add_review/<item_id>', views.add_review, name='add_review'),
    path(
        'edit_review/<int:review_items_id>/', views.edit_review,
        name='edit_review'
    ),
    path(
        'confirmation/<item_id>', views.delete_review_confirmation,
        name='delete_review_confirmation'
    ),
    path(
        'delete_review/<int:review_items_id>/', views.delete_review,
        name='delete_review'
    ),
]
