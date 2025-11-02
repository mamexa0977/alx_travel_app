from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price_per_night', 'property_type',
            'bedrooms', 'bathrooms', 'max_guests', 'address', 'city', 'country',
            'latitude', 'longitude', 'amenities', 'is_available', 'created_at'
        ]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'guest_name', 'guest_email', 'check_in', 
            'check_out', 'total_price', 'status', 'created_at'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'listing', 'guest_name', 'rating', 'comment', 'created_at']