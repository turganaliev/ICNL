from rest_framework import serializers

from NPO.models import News, NewsImage, TypeLaw, Law, Publication


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title short_text created image'.split()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = 'id image'.split()


class NewsDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = News
        fields = 'id title text created link images'.split()


class TypeLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLaw
        fields = 'id name'.split()


class LawsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text'.split()


class LawDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text law_type'.split()


class PublicationsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file'.split()


class PublicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file types'.split()