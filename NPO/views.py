from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from NPO.models import News, TypeLaw, Law, Publication, FavouriteNews
from rest_framework.response import Response
from NPO.serializers import NewsSerializer, NewsDetailSerializer, TypeLawSerializer, LawDetailSerializer, \
    LawsByTypeSerializer, PublicationsByTypeSerializer, PublicationDetailSerializer


class NewsCreateAPI(APIView, PageNumberPagination):
    def get(self, request):
        search = request.query_params.get('search', '')
        news = News.objects.filter(Q(title__icontains=search) |
                                   Q(text__icontains=search))
        results = self.paginate_queryset(news, request, view=self)
        data = NewsSerializer(results, many=True, context={'request': request}).data
        return self.get_paginated_response(data)


class NewsDetailAPI(APIView):
    def get(self, request, id):
        news = News.objects.get(pk=id)
        data = NewsDetailSerializer(news).data
        return Response(data=data)


class TypeLawAPI(APIView):
    def get(self, request):
        types = TypeLaw.objects.all()
        data = TypeLawSerializer(types, many=True).data
        return Response(data=data)


class LawsByTypeAPI(APIView):
    def get(self, request):
        search = request.query_params.get('type_id', '')
        laws = Law.objects.filter(law_type=search)
        data = LawsByTypeSerializer(laws, many=True).data
        return Response(data=data)


class LawDetailAPI(APIView):
    def get(self, request, id):
        law = Law.objects.get(pk=id)
        data = LawDetailSerializer(law).data
        return Response(data=data)


class PublicationsByTypeAPI(APIView):
    def get(self, request):
        search = request.query_params.get('type_id', '')
        publications = Publication.objects.filter(types=search)
        data = PublicationsByTypeSerializer(publications, many=True).data
        return Response(data=data)


class PublicationDetailAPI(APIView):
    def get(self, request, id):
        publication = Publication.objects.get(pk=id)
        data = PublicationDetailSerializer(publication).data
        return Response(data=data)


class NewsFavouriteAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        news_id = request.data.get('news_id')
        try:
            favourite = FavouriteNews.objects.get(news_id=news_id, user=request.user)
            print('GET')
        except:
            favourite = FavouriteNews.objects.create(news_id=news_id, user=request.user)
            print('CREATE')
        favourite.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        news_id = request.data.get('news_id')
        favourite = FavouriteNews.objects.filter(news_id=news_id, user=request.user)
        favourite.delete()
        return Response(status=status.HTTP_200_OK)