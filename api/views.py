from rest_framework.decorators import api_view
from rest_framework.response import Response

from web.models import Borrow

from api.serializers import BorrowSerializer


@api_view(["GET"])
def main_view(request):
    return Response({"status":"ok"})

@authetication_classes([SessionAuthetication, TokenAuthetication])
@permissions([IsAutheticated])
@api_view(["GET"])
def borrow_view(request):
    borrow = Borrow.objects.all()

    serializer = BorrowSerializer(borrow,many=True)
    return Response(serializer.data)