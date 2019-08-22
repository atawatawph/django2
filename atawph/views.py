from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.utils.translation import gettext as _

def post_list(request):
    from django.utils import translation
    user_language = ''
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    home = _('Home')
    about = _('About')
    organization = _('Organization')
    career = _('Career')
    contact = _('Contact')
    posts = ('post')
    

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts':posts, 'home': home, 'about': about, 'organization': organization, 'career': career, 'contact': contact, })
    #'mission': mission, 'vision': vision, 'admin': admin

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

# Create your views here.
