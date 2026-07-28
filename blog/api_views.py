# blog/api_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Posted
from .serializers import PostSerializer

# সব published posts
@api_view(['GET'])
def post_list_api(request):
    search = request.query_params.get('search', '')
    posts  = Posted.objects.filter(
        status='published',
        title__icontains=search
    )
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# একটা post detail
@api_view(['GET'])
def post_detail_api(request, pk):
    try:
        post = Posted.objects.get(id=pk, status='published')
    except Posted.DoesNotExist:
        return Response({'error': 'Post পাওয়া যায়নি'}, status=404)

    serializer = PostSerializer(post)
    return Response(serializer.data)