from blog.models import Post
from rest_framework import viewsets
from blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer