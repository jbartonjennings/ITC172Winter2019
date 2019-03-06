from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting
from .forms import MeetingForm, ResourceForm

# Create your views here.

def index(request):
    return render(request, 'club/index.html')

def resource(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resource.html', {'resource_list':resource_list})

def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render (request, 'club/meeting.html', {'meeting_list':meeting_list})    

def meetingdetail(request, id):
    detail=get_object_or_404(Meeting, pk=id)
    context = {'detail': detail}
    return render (request, 'club/details.html', context=context)

#form view
def newMeeting(request)
    form=MeetingForm
    if request.method=='POST':
        form.MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def newResource(request)
    form=ResourceForm
    if request.method=='POST':
        form.ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})



