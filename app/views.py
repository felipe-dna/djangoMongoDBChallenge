from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import ModelFormMixin

from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy

from django.contrib import messages

from .models import Video, Theme
from.forms import VideoCreateForm

# views

class HomeView(ListView):
    model = Video
    template_name = 'app/home.html'
    context_object_name = 'videos'

    def get_success_url(self: object):
        return reverse('app:watch', kwargs={'uuid': self.object.pk})

    def get_context_data(self: object, **kwargs) -> object:
        context = super().get_context_data(**kwargs)
        context['form'] = VideoCreateForm()

        return context



class WatchVideoView(DetailView):
    model = Video
    template_name = 'app/video.html'
    context_object_name = 'video'



def uploadView(request):
    form = VideoCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    
    return HttpResponseRedirect(reverse('app:home'))



def thumbUp(request, pk):
    video = Video.objects.filter(id=pk).first()
    video.thumbs_up += 1
    video.save()

    # Sending a success message
    message = "+1 thumbs up on {}".format(video.name)
    messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse('app:home'))


def thumbDown(request, pk):
    video = Video.objects.filter(id=pk).first()
    video.thumbs_down += 1
    video.save()

    # Sending a success message
    message = "+1 thumbs down at {}".format(video.name)
    messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse('app:home'))
