from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST

from django.http import HttpResponseRedirect
from django.shortcuts import reverse

from django.contrib import messages

from .models import Video, Theme
from.forms import VideoUploadForm, ThemeForm

# views


# + ------------------------------------------------------------------------- +
class HomeView(ListView):
    """
    View que renderiza a página inicial. Retorna uma lista com todos os vídeos
    cadastrados ordenados pela data de upload e um formulário para fazer
    upload de mais vídeos.
    """
    model = Video
    template_name = 'app/home.html'
    queryset = Video.objects.all().order_by('-uploaded_at')
    context_object_name = 'videos'
    paginate_by = 6

    # Adding an form instance to context.
    def get_context_data(self: object, **kwargs) -> object:
        context = super().get_context_data(**kwargs)
        context['form'] = VideoUploadForm()

        return context
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class WatchVideoView(DetailView):
    model = Video
    template_name = 'app/video.html'
    context_object_name = 'video'
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class ThemeListView(ListView):
    model = Theme
    template_name = 'app/theme-list.html'
    context_object_name = 'themes'
    queryset = Theme.objects.all().order_by('-score')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ThemeForm()
        return context

# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class ThemeDetailView(DetailView):
    model = Theme
    template_name = 'app/theme.html'
    context_object_name = 'theme'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["video_list"] = Video.objects.filter(
                                    theme__id=context['theme'].id) 
        return context
    
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
@require_POST
def uploadView(request):
    form = VideoUploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

        message = "New video uploaded successfully!"
        messages.add_message(request, messages.SUCCESS, message)
    
    return HttpResponseRedirect(reverse('app:home'))
# + ------------------------------------------------------------------------- +

# + ------------------------------------------------------------------------- +
@require_POST
def createThemeView(request):
    form = ThemeForm(request.POST)
    
    if form.is_valid():
        form.save()

        message = "New theme registred successfully!"
        messages.add_message(request, messages.SUCCESS, message)
    
    return HttpResponseRedirect(reverse('app:themes'))
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
def thumbUp(request, pk):
    video = Video.objects.filter(id=pk).first()
    video.thumbs_up += 1
    video.save()

    # Sending a success message
    message = "+1 thumbs up on {}".format(video.name)
    messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse('app:watch', kwargs={'pk': video.id}))
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
def thumbDown(request, pk):
    video = Video.objects.filter(id=pk).first()
    video.thumbs_down += 1
    video.save()

    # Sending a success message
    message = "+1 thumbs down on {}".format(video.name)
    messages.add_message(request, messages.WARNING, message)

    return HttpResponseRedirect(reverse('app:watch', kwargs={'pk': video.id}))
# + ------------------------------------------------------------------------- +
