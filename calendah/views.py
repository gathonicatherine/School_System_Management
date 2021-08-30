from datetime import date
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from .forms import EventForm
from .models import *
from .utils import Calendar
 
# Create your views here.
 
 
class CalendarView(generic.ListView):
   model = Event
   template_name = 'event_list.html'
 
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
      
 
      
       d = get_date(self.request.GET.get('day', None))
 
 
       cal = Calendar(d.year, d.month)
 
  
       html_cal = cal.formatmonth(withyear=True)
       context['calendar'] = mark_safe(html_cal)
       return context
 
def get_date(req_day):
   if req_day:
       year, month = (int(x) for x in req_day.split('-'))
       return date(year, month, day=1)
   return datetime.today()
 
def event(request, event_id=None):
   instance = Event()
   if event_id:
       instance = get_object_or_404(Event, pk=event_id)
   else:
       instance = Event()
       form = EventForm(request.POST or None, instance=instance)
   if request.POST and form.is_valid():
       form.save()
       return redirect('cal:calender')
      
   return render(request, 'add_event.html', {'form': form})