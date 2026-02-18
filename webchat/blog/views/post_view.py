from django.http import HttpResponse
from django.views import generic

from blog.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

class PostDetail(generic.DetailView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"