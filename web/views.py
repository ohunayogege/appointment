from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import AppointmentSerializer
from .models import Appointment


# class MakeAppointment(APIView):
#     def get_object(self, pk):
#         try:
#             return Appointment.objects.get(pk=pk)
#         except Appointment.DoesNotExist:
#             raise Http404
#
#     def post(self, request):
#         serializer = AppointmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'success', 'message': 'New Appointment Added',\
#              'data': serializer.data}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'status': 'error', 'message': serializer.errors},\
#             status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         id = request.GET.get('appointment_id')
#         if id:
#             check_id = Appointment.objects.filter(id=id).exists()
#             if check_id == False:
#                 return Response({'status': 'error', 'message': 'No appointment with such ID'},\
#                 status=status.HTTP_404_NOT_FOUND)
#             appointment = Appointment.objects.get(id=id)
#             serializer = AppointmentSerializer(appointment, many=False)
#             return Response({'status': 'success', 'message': 'fetched appointment', 'data': serializer.data},\
#             status=status.HTTP_200_OK)
#         else:
#             appointment = Appointment.objects.all()
#             serializer = AppointmentSerializer(appointment, many=True)
#             return Response({'status': 'success', 'message': 'fetched all appointments', 'data': serializer.data},\
#             status=status.HTTP_200_OK)
#
#     def patch(self, request, pk, format=None):
#         appointment = self.get_object(pk)
#         print(appointment)
#         serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'success', 'message': 'Appointment updated successful.', 'data': serializer.data},\
#             status=status.HTTP_200_OK)
#
#     def delete(self, request, pk, format=None):
#         appointment = self.get_object(pk)
#         appointment.delete()
#         appointment.save()
#         return Response({'status': 'success', 'message': 'deleted successful'},\
#         status=status.HTTP_204_NO_CONTENT)


class MakeAppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request):
    	serializer = AppointmentSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response({'status': 'success', 'message':'New appointment created.', 'data': serializer.data})
    	else:
    		return Response({'status': 'error', 'message':serializer.errors})

    def list(self, request, *args, **kwargs):
    	name = self.request.query_params.get('name')
    	if name:
    		query = Appointment.objects.filter(name__icontains=name)
    		serializer = AppointmentSerializer(query, many=True)
    		return Response({'status': 'success', 'message':'fetched single appointment', 'data': serializer.data})
    	appointment = Appointment.objects.all()
    	serializer = AppointmentSerializer(appointment, many=True)
    	return Response({'status': 'success', 'message':'fetched all appointments', 'data': serializer.data})

    def retrieve(self, request, *args, **kwargs):
    	try:
    		appointment = self.get_object()
    		serializer = AppointmentSerializer(appointment, many=False)
    	except:
    		return Response({'status': 'error', 'message':serializer.errors})
    	return Response({'status': 'success', 'message':'fetched single appointment', 'data': serializer.data})

    def partial_update(self, request, *args, **kwargs):
    	try:
    		appointment = self.get_object()
    		serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
    		serializer.is_valid()
    		serializer.save()
    	except:
    		return Response({'status': 'error', 'message': 'No Appointment with such ID'}, status=status.HTTP_404_NOT_FOUND)
    	return Response({'status': 'success', 'message':'updated successfully', 'data': serializer.data})

    def destroy(self, request, *args, **kwargs):
    	try:
    		appointment = self.get_object()
    		self.perform_destroy(appointment)
    	except:
    		return Response({'status': 'error', 'message': 'No Appointment with such ID'}, status=status.HTTP_404_NOT_FOUND)
    	return Response({'status': 'success', 'message': 'deleted successfully'})
