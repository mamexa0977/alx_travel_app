from django.contrib import admin
from .models import Listing, ListingImage, Booking, Review

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'price_per_night', 'city', 'is_available']
    list_filter = ['property_type', 'city', 'is_available']
    search_fields = ['title', 'description', 'city']

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ['listing', 'is_primary']
    list_filter = ['is_primary']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['guest_name', 'listing', 'check_in', 'check_out', 'status']
    list_filter = ['status', 'check_in', 'check_out']
    search_fields = ['guest_name', 'guest_email']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['guest_name', 'listing', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['guest_name', 'comment']