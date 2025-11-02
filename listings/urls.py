from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingList.as_view(), name='listing-list'),
    path('<int:pk>/', views.ListingDetail.as_view(), name='listing-detail'),
    path('bookings/', views.BookingCreate.as_view(), name='booking-create'),
    path('reviews/', views.ReviewCreate.as_view(), name='review-create'),
]