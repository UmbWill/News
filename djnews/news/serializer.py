from rest_framework.serializers import ModelSerializer
from .models import News

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = (
            'source_id',
            'source_name',
            'author',
            'title',
            'description',
            'url',
            'urlToImage',
            'publishedAt',
            'content'
        )