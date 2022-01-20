from rest_framework.views import APIView
from rest_framework import authentication, permissions
from articles.models import Articles
from rest_framework.response import Response
from articles.serializer import CategorySerializer, ArticleSerializer


class ListArticle(APIView):
    """
    View para listar todos os artigos publicados

    * Requer autenticação de token.
    * Somente usuários autenticados podem acessar esta visualização.
    """

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, format=None):
        """
        Retorna a lista de todos os artigos publicados
        """
        list_articles = Articles.objects.filter(publish=True)
        serializer = ArticleSerializer(list_articles, many=True)
        return Response(serializer.data)
