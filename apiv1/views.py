from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import *


# Create your views here.

class TextCreate(CreateAPIView):
    serializer_class = TextSerializer
    allowed_methods = ["POST"]
    queryset = Text.objects.all()


class TextList(ListAPIView):
    serializer_class = TextSerializer
    queryset = Text.objects.all()
