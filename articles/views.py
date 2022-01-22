from rest_framework.views import APIView
from django.http import Http404
from articles.models import Articles
from rest_framework.response import Response
from articles.serializer import CategorySerializer, ArticleSerializer
from rest_framework import status


class ListArticle(APIView):
    """
    API View de Artigos
    """

    def get_queryset(self):
        """
        Busca todos os artigos publicados
        """
        list_articles = Articles.objects.filter(publish=True)
        return list_articles

    def get_object(self, pk):
        try:
            return Articles.objects.get(pk=pk)
        except Articles.DoesNotExist:
            raise Http404

    def get(self, request):
        """
        Retorna todos os artigos publicados
        """
        list_articles = self.get_queryset()
        serializer = ArticleSerializer(list_articles, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
