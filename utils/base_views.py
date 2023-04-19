from rest_framework.views import APIView, Request, Response, status


class CreateBaseView(APIView):
    view_serializer = None
    
    def create(self, request: Request) -> Response:
        """
        Registro de usuários
        """
        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)