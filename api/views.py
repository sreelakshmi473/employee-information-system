from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from work.models import Employeemodel
from api.serializer import Emp_serializer
from rest_framework.viewsets import ViewSet


class employeeviewsetview(ViewSet):
    def list(self,request,*args,**kwargs):
      qs=Employeemodel.objects.all()
      serializers=Emp_serializer(qs,many=True)
      return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
       serializers=Emp_serializer(data=request.data)
       if serializers.is_valid():
          serializers.save()
          return Response(data=serializers.data)
       return Response(serializers.errors)
    
    def retrieve(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       qs=Employeemodel.objects.get(id=id)
       serializers=Emp_serializer(qs)
       return Response(data=serializers.data)
      #  return Response(serializers.errors)
    
    def update(self,request,*args,**kwargs):
      id=kwargs.get("pk")
      qs=Employeemodel.objects.get(id=id)
      serializers=Emp_serializer(data=request.data,instance=qs)
      if serializers.is_valid():
        serializers.save()
        return Response(data=serializers.data)
      return Response(serializers.errors)
    
    def delete(self,request,*args,**kwargs):
      id=kwargs.get("pk")
      Employeemodel.objects.get(id=id).delete()
      return Response("employee deleted sucessfully")



# class employee_apiview(APIView):
#   def get(self,request,*args,**kwargs):
#     qs=Employeemodel.objects.all()
#     serilizers=Employee_serializer(qs,many=True)
#     return Response(data=serilizers.data)
#   def post(self,request,*args,**kwargs):
#     serializers=Employee_serializer(data=request.data)
#     if serializers.is_valid():
#       serializers.save()
#     return Response(serializers.data)
  
# class Employee_mixin(APIView):
#     def get(self,request,*args,**kwargs):
#       id=kwargs.get("pk")
#       qs=Employeemodel.objects.get(id=id)
#       serilizers=Employee_serializer(qs)
#       return Response(data=serilizers.data)
    
#     def delete(self,request,*args,**kwargs):
#       id=kwargs.get("pk")
#       Employeemodel.objects.get(id=id).delete()
#       return Response("employee deleted sucessfully")
    
#     def put(self,request,*args,**kwargs):
#       id=kwargs.get("pk")
#       qs=Employeemodel.objects.get(id=id)
#       serializers=Employee_serializer(data=request.data,instance=qs)
#       if serializers.is_valid():
#         serializers.save()
#         return Response(data=serializers.data)
#       return Response(serializers.errors)
# 












# class Employee_view(APIView):
#     def get(self,request,*args,**kwargs):
#         qs=Employeemodel.objects.all()
#         serializers=Emp_serializer(qs,many=True)
#         return Response(data=serializers.data)
#     def post(self,request,*args,**kwargs):
#         serializers=Emp_serializer(data=request.data)
#         if serializers.is_valid():
#            serializers.save()
#            return Response(data=serializers.data)
#         return Response(serializers.errors)
    
