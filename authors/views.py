from rest_framework.views import APIView
from authors.models import Author
from authors.serializer import AuthorSerializer
from rest_framework.response import Response


class ListAuthor(APIView):
    """
    Lista todos os autores ativos
    """

    def get(self, request, format=None):
        """
        Retorna a lista de autores ativos
        """
        list_author = Author.objects.filter(status=True)
        serializer = AuthorSerializer(list_author, many=True)
        return Response(serializer.data)
