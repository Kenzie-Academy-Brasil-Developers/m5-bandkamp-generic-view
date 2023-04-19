from rest_framework.views import APIView, Request, Response

from utils.base_views import CreateBaseView


class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None


class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request: Request) -> Response:
        return super().create(request)
    
    