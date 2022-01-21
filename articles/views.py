from rest_framework.views import APIView
from articles.models import Articles
from rest_framework.response import Response
from articles.serializer import CategorySerializer, ArticleSerializer


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

    def get(self, request, *args, **kwargs):
        """
        Retorna todos os artigos publicados
        """
        list_articles = self.get_queryset()
        serializer = ArticleSerializer(list_articles, many=True)
        return Response(serializer.data)
