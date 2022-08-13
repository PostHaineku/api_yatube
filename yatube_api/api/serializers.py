from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('text', 'pub_date', 'author', 'group')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'created')
