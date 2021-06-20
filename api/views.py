from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

from .models import Post


@api_view(['GET'])
def postkList(request):
	posts = Post.objects.all().order_by('-id')
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)