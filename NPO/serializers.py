from rest_framework import serializers

from NPO.models import News, NewsImage, TypeLaw, Law, Publication, FavouriteNews


class NewsSerializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title short_text created image is_favourite'.split()

    def get_is_favourite(self, obj):
        request = self.context['request']
        if request.user.is_anonymous:
            return False
        else:
            favourites = FavouriteNews.objects.filter(user=request.user, news=obj)
            count = favourites.count()
            print(count, favourites)
            if count > 0:
                return True
            else:
                return False


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