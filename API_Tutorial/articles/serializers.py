from rest_framework import serializers
from .models import Article

"""
class Article_serializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.description = validated_data.get("description",instance.description)
        instance.body = validated_data.get("body",instance.body)
        #instance.author_id = validated_data.get("author_id",instance.author_id)
        instance.save()
        return instance
"""
class Article_serializer(serializers.ModelSerializer):
    class Meta():
        model = Article
        fields = ("title", "description", "body", "author")