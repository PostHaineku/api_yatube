from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='slug'
    )

    class Meta:
        model = Post
        fields = '__all__'
# В теории наоборот писали что намного лучше мануально прописывать поля
# Мол явное лучше неявного))


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
