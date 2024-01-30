from django.db import models

class TicketModel(models.Model):

    Status_view =(
        ('none' , 'None'),
        ('pending' , 'Pending'),
        ('inprogress' , 'In Progress'),
        ('success' , 'Completed')
    )
    Prioritylevel = (
        ('none' , 'None'),
        ('low' , 'Low'),
        ('medium' , 'Medium'),
        ('high' , 'High')
    )
    Ticket_ID = models.IntegerField()
    Name = models.CharField(max_length=100 )
    Reason = models.TextField()
    Reason_Description = models.TextField()
    Appeared_Time = models.DateTimeField()
    Priority_Scales = models.CharField(max_length=100 , choices=Prioritylevel , default=None)
    Status = models.CharField(max_length=100 , choices=Status_view , default=None)
    Reporter = models.TextField(default=None)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
