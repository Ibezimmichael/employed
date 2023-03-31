from rest_framework import generics, status, mixins
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from .observers import send_new_employee_notification

@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):

    if request.method == "POST":
        data = request.data

        response = {"message": "Hello World", "data": data}

        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    

class EmployeeDetail(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'name'
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class EmployeeDetailDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'name'
    permission_classes = [IsAuthenticated]
    

class EmployeesByDepartment(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]
    lookup_field = 'department'

    def get_queryset(self):
        department = self.kwargs.get('department')
        return Employee.objects.filter(department__slug=department)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

