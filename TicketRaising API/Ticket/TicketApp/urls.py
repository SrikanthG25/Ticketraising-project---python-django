from django.urls import path
from . views import *

urlpatterns = [
    path('ticketraising/' , TicketView.as_view() , name='TicketRaising'),
    path('ticketraising/<int:pk>/' , TicketView.as_view() , name='Ticket_Details'),
    path('status/' , statusView.as_view()),
    # path('Email/' , SendMail.as_view())

]