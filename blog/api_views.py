# blog/api_views.py

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
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

# Post edit করো (Login লাগবে)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def post_edit_api(request, pk):
    try:
        post = Posted.objects.get(id=pk, author=request.user)
    except Posted.DoesNotExist:
        return Response({'error': 'Post পাওয়া যায়নি'}, status=404)

    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Post delete করো (Login লাগবে)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def post_delete_api(request, pk):
    try:
        post = Posted.objects.get(id=pk, author=request.user)
        post.delete()
        return Response({'message': 'Post delete হয়েছে!'})
    except Posted.DoesNotExist:
        return Response({'error': 'Post পাওয়া যায়নি'}, status=404)
