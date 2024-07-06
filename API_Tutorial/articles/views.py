from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.views import APIView
from .models import Article,Author
from .serializers import Article_serializer

# Create your views here.
"""
APIView
class ArticleView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serialized_data = Article_serializer(articles,many = True)
        return Response({"value":serialized_data.data})
    
    def post(self,request):
        article = request.data.get("article")
        serialized = Article_serializer(data=article)
        if serialized.is_valid(raise_exception=True):
            saved=serialized.save()
            print(saved)
        return Response({"data":"Saved in DB"})
    
    def put(self, request, pk):
        print(request)
        saved_article = get_object_or_404(Article.objects.all(),pk = pk)
        data = request.data.get("article")
        serialized_data = Article_serializer(instance=saved_article,data=data,partial = True)
        if serialized_data.is_valid(raise_exception=True):
            saved = serialized_data.save()
        return Response({"data":"Updated data"}) 
    
    def delete(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(),pk = pk)
        saved_article.delete()
        return Response({"detail":"Item {} deleted".format(pk)})
"""

"""
#mixins
class ArticleView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    
    def get(self,request):
        return self.list(request)
    def post(self,request):
        print("Posted")
        return self.create(request)
"""
class ArticleView(ListCreateAPIView):
    """
        This GenericAPIView performs get(many) and creates(many)
    """
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    
class SingleArticleView(RetrieveUpdateAPIView):
    """
        This GenericAPIView performs get(single) and updates(single)
    """
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    