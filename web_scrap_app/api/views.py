from rest_framework.response import Response
from .. import models
from rest_framework import generics
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from . import paginations


class BlogView(generics.GenericAPIView):
    serializer_class = serializers.BlogViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "author_name", "author_designation"]
    ordering_fields = ["title", "read_time"]
    ordering = "id"

    def get(self, request, *args, **kwargs):
        blogs_db = models.Blog.objects.all()
        paginator = paginations.CustomPageNumberPagination()
        blogs = self.filter_queryset(blogs_db)
        result = paginator.paginate_queryset(blogs, request)
        serializer = self.serializer_class(instance=result, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Successfully saved", "data": serializer.data}, status=201
            )
        return Response(
            {"message": "Invalid data provided", "errors": serializer.errors},
            status=400,
        )


class BlogDetailView(generics.GenericAPIView):
    serializer_class = serializers.BlogViewSerializer

    def get(self, request, id, *args, **kwargs):
        blogs = models.Blog.objects.filter(id=id).first()
        if not blogs:
            return Response({"message": "Couldnot find data"}, status=404)
        serializer = self.serializer_class(blogs)
        return Response(
            {"message": "Successfully fetched", "data": serializer.data}, status=200
        )

    def put(self, request, id, *args, **kwargs):
        blogs = models.Blog.objects.filter(id=id).first()
        if not blogs:
            return Response({"message": "Couldnot find data"}, status=404)
        serializer = self.serializer_class(
            instance=blogs, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Successfully fetched", "data": serializer.data}, status=200
            )
        return Response(
            {"message": "Invalid data provided", "errors": serializer.errors},
            status=400,
        )

    def delete(self, request, id, *args, **kwargs):
        blogs = models.Blog.objects.filter(id=id).first()
        if not blogs:
            return Response({"message": "Couldnot find data"}, status=404)
        blogs.delete()
        return Response({"message": "Successfully deleted"}, status=200)
