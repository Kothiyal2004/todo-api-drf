from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Todo
# from .serializers import TodoSerializer

# ✅ PUT: Full update
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=404)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# ✅ DELETE: Remove record
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return Response({'message': 'Todo deleted successfully'})
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=404)

# ✅ PATCH: Partial update
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=404)

    serializer = TodoSerializer(todo, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



