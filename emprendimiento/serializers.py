from rest_framework import serializers

from .models import User, Emprendimiento, Review, User2

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = '__all__'
