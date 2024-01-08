from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apartments.base_classes import CustomPermission
from housing.models import *
from housing.serializers import *

# Create your views here.
class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    permission_classes = [CustomPermission]

    def partial_update(self, request, pk, *args, **kwargs):
        '''
            Method that updates the object only if is owned by the
            user that created the request.
        '''
        ap = Apartment.objects.get(pk=pk)
        if ap.owner != request.user:
            return Response({'error': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, pk, *args, **kwargs)

    @action(methods=['PATCH'], detail=True)
    def set_unavailable(self, request, pk):
        '''
            Method that sets an appartment as unavailable
        '''
        apartment = Apartment.objects.get(pk=pk)
        user = request.user
        if user.role == 'admin' or apartment.owner == user:
            apartment.is_available = False
            apartment.save()
            return Response(ApartmentSerializer(apartment).data, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
    @action(methods=['PATCH'], detail=True)
    def set_available(self, request, pk):
        '''
            Method that sets an apartment as available
        '''
        apartment = Apartment.objects.get(pk=pk)
        user = request.user
        if user.role == 'admin' or apartment.owner == user:
            apartment.is_available = True
            apartment.save()
            return Response(ApartmentSerializer(apartment).data, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [CustomPermission]

    def create(self, request):
        '''
            Method that creates a new reservation
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            apartment = data['apartment']
            
            if not apartment.is_available:
                return Response({'error': 'apartment not available to make reservation'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = data['customer']
            if user.role == 'customer':
                qs = Reservation.objects.filter(apartment=apartment)
                if len(qs) == 0:
                    serializer.save()
                    return Response(data, status=status.HTTP_201_CREATED)
                
                qs1 = qs.filter(start_date__lte=data['start_date'])
                qs2 = qs.filter(start_date__gte=data['start_date'])
                available = not qs1.filter(end_date__gte=data['start_date']).exists()
                available = available and not qs1.filter(end_date__gte=data['end_date']).exists()
                available = available and not qs1.filter(end_date__gte=data['start_date'], end_date__lte=data['end_date']).exists()
                available = available and not qs2.filter(start_date__lte=data['end_date']).exists()
                available = available and not qs2.filter(end_date__lte=data['end_date']).exists()

                if available:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                return Response({'error': 'apartment not available in the timespan specified'}, status=status.HTTP_400_BAD_REQUEST)
            