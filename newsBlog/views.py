from django.shortcuts import render, get_object_or_404
from .models import News, IP, Tag


# функция получения ip пользователя, возможно стоило сделать декоратором
def get_ip(request):
    http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_x_forwarded_for:
        ip = http_x_forwarded_for.split(',')[0]  # сплит для получения только айпи, без прокси
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def view(request):
    news = News.objects.all()
    return render(request, 'main.html', {'news': news})


def post(request, slug):
    exact_post = get_object_or_404(News, slug=slug)
    ip = get_ip(request)
    if IP.objects.filter(IpName=ip).exists():
        exact_post.views.add(IP.objects.get(IpName=ip))
    else:
        IP.objects.create(IpName=ip)
        exact_post.views.add(IP.objects.get(IpName=ip))
    return render(request, 'post.html', {'exact_post': exact_post})


def tag(request, tag_id):
    news_objects = News.objects.filter(tags__id=tag_id)
    current_tag = Tag.objects.get(id=tag_id)
    return render(request, 'tags.html', {'news_obj': news_objects, 'curr_tag': current_tag})


def viewsCount(request):
    news = News.objects.all()
    for n in News.objects.all():
        n.total_views()
    return render(request, 'listWithViews.html', {'news': news})
