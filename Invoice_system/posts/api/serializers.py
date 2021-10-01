from rest_framework import serializers
from ..models import Post

class PostModelserializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields=['id','title','description','created','author']

