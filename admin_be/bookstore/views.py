from rest_framework import mixins,generics
from .models import Book
from .serializer import BookSerializer
from .mixins import BookstoreMixin

class BookListCreateView(BookstoreMixin,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self,request,*args,**kwargs):

        self.log_action("List","All Books")
        return self.list(request,*args,**kwargs)

    def post(self,request, *args,**kwargs):
        response = self.create(request,*args,**kwargs)
        if response.status_code == 201:
            book_title = response.data.get('title', 'Unknown title')
            self.log_action("Create",book_title)
        return response
