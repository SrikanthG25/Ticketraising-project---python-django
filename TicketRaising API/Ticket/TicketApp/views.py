from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import *
from .serializers import *

from django.core.mail import send_mail
from django.conf import settings


class TicketView(generics.GenericAPIView):
    queryset = TicketModel.objects.all()
    serializer_class = TicketSerializers
    def post(self , request):

        '''
        URL : http://127.0.0.1:8000/ticketraising/

        {
            "Name": "s",
            "Reason": "s",
            "Reason_Description": "s",
            "Appeared_Time": "2023-10-10T16:35:00Z",
            "Priority_Scales": "low",
            "Status": "pending",
            "Reporter": "s"
        }
        '''
        try:
            ticket_num =  TicketModel.objects.filter().aggregate(max_num =Max('Ticket_ID'))['max_num'] or 0
            request.data['Ticket_ID'] = ticket_num + 1 
            tickets = TicketSerializers(data=request.data)
            tickets.is_valid()
            tickets.save()
            print(tickets,"???????????????????????/////")
            return Response({'message':'Successfull send the Ticket','data': tickets.data} , status=status.HTTP_200_OK)
        except :
            return Response({'Messsge' : 'Fill the data'} , status=status.HTTP_501_NOT_IMPLEMENTED)

    def get(self , request , pk=None):
        try:
            if pk is not None:
                Ticket = TicketModel.objects.filter(pk = pk)
                serializer = TicketSerializers(Ticket , many=True)
                return Response(serializer.data)
            else:
                Ticket = TicketModel.objects.all()
                serializer = TicketSerializers(Ticket , many=True)
                return Response(serializer.data)
        except Exception:
            return Response({'message' : 'Client Not Found , Given valid ID'} , status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk=None):
        try:
            if pk is not None:
                ticket = TicketModel.objects.get(pk=pk)
                serializer = TicketSerializers(ticket, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        except TicketModel.DoesNotExist:
            return Response({'message': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request , pk=None):
        try:
            if pk is not None:
                ticket = TicketModel.objects.get(pk=pk)
                ticket.delete()
                return Response({'message': 'Ticket deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'ID Not Found'}, status=status.HTTP_400_BAD_REQUEST)
        except TicketModel.DoesNotExist:
            return Response({'message': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)


#status updating in postman query based function
class statusView(generics.GenericAPIView):
    def put(self , request):
        try: 
            data =request.query_params
            id = data.get('id')
            stat = data.get('Status')
            ticket = TicketModel.objects.filter(id=id).values('Ticket_ID','Name','Reason','Reason_Description','Appeared_Time','Priority_Scales','Status')
            ticket.update(Status=stat)
            return Response({'message':'Status successfully Updated'}, status = status.HTTP_200_OK)
        except Exception:
            return Response({'message' : 'Status Not Update'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

#Email send function in automatic post the ticket in postman
# class SendMail(generics.GenericAPIView):
#     def post(self, request):
#         ticket_num =  TicketModel.objects.filter().aggregate(max_num =Max('Ticket_ID'))['max_num'] or 0
#         request.data['Ticket_ID'] = ticket_num + 1 
#         serializer = TicketSerializers(data=request.data)
#         if serializer.is_valid():
#             ticket=serializer.save()
#             subject = 'New Ticket Created'
#             # message = f'A new ticket has been created with : {ticket}-- \n\n,{serializer.data}'
#             message = (
#                 f'A new ticket has been created with : {ticket}\n\n'
#                 f'Ticket ID :  {ticket.Ticket_ID}\n'
#                 f'Name : {ticket.Name}\n'
#                 f'Reason : {ticket.Reason}\n'
#                 f'Reason Description : {ticket.Reason_Description}\n'
#                 f'Appeared Time : {ticket.Appeared_Time}\n'
#                 f'Priority Scales : {ticket.Priority_Scales}\n'
#                 f'Status : {ticket.Status}\n'
#                 f'Reporter : {ticket.Reporter}\n'
#                 f'Created : {ticket.Created}\n\n\n\n'
#                 f'Looking forward to hearing from you \n Thank You ...\n'
#             )
#             from_email = 'settings.EMAIL_HOST_USER'
#             recipient_list =  [settings.EMAIL_HOST_USER]         

#             send_mail(subject, message, from_email , recipient_list)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class statusView(generics.GenericAPIView):
    def put(self , request):
        try: 
            data =request.query_params
            id = data.get('id')
            status = data.get('Status')
            data = {
                'id' : id,
                'Status' : status 
            }
            Update_Data = TicketModel(**data)
            Update_Data.save()
            
            # ticket = TicketModel.objects.filter(id=id).values('Status')
            return Response(Update_Data.data)
        except Exception:
            return Response({'message' : 'Status Not Update'})

'''



    #  data =request.query_params
    #         id = data.get('id')
    #         status = data.get('Status')
    #         ticket = TicketModel.objects.filter(id=id).values('Ticket_ID','Name','Reason','Reason_Description','Appeared_Time','Priority_Scales','Status')
    #         ticket['Status']=status
    #         print(ticket)
    #         # data = {
    #         #     'id' : id,
    #         #     'Status' : status 
    #         # }
    #         Update_Data = TicketModel(**ticket)
    #         Update_Data.save()

    #         # ticket = TicketModel.objects.filter(id=id).values('Status')
    #         return Response(Update_Data.data)

