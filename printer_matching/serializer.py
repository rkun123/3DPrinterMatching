from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    lat = serializers.FloatField(required=True)
    lng = serializers.FloatField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'lat': self.validated_data.get('lat', ''),
            'lng': self.validated_data.get('lng', '')
        }