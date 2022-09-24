from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()


    class Meta:
        model = Profile
        fields = [
            'posts_count', 'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'followers_count', 'following_count'
        ]