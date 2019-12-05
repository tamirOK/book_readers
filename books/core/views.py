from rest_framework import generics
from rest_framework_csv import renderers


from .models import Book, Reader
from .serializers import BookSerializer, ReaderSerializer


class ReaderDetail(generics.RetrieveAPIView):
    queryset = Reader.objects.all().prefetch_related('books')
    serializer_class = ReaderSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookExport(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    renderer_classes = (renderers.PaginatedCSVRenderer,)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        response["Content-Disposition"] = "attachment; filename=books.csv"
        return response


class ReaderExport(generics.ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    renderer_classes = (renderers.PaginatedCSVRenderer,)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        response["Content-Disposition"] = "attachment; filename=readers.csv"
        return response
