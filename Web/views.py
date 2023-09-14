from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *
import markdown
import re


def test(request):
    return render(request, 'test.html')


def home(request):
    img_list = IndexImgCarousel.objects.all()
    introduction = LabIntroduction.objects.all()
    if len(introduction) > 0:
        introduction = introduction[0]
    else:
        introduction = '暂时没有简介'
    LabProprietarySystem_list = LabProprietarySystem.objects.all()

    latest_news_list = News.objects.order_by("-pubdate")[:5]

    return render(request, 'home.html', {'img_list': img_list, 'introduction': introduction,
                                         'LabProprietarySystem_list': LabProprietarySystem_list,
                                         'latest_news_list': latest_news_list})


def research_dir(request):
    return render(request, 'research.html')


def team_t_s(request):
    return render(request, 'team_t_s.html')


def thesis(request):
    return render(request, 'thesis.html')


def personnel_training(request):
    return render(request, 'train.html')


def news(request):
    news_list = News.objects.order_by("-pubdate")
    paginator = Paginator(news_list, 10)
    page_number_raw = request.GET.get("page")

    if not page_number_raw:
        page_obj = paginator.get_page(1)
        return render(request, 'news.html', {"news_list": page_obj})

    try:
        page_number = re.match('\\d+', page_number_raw)
        page_number = int(page_number.group())

        if page_number > paginator.num_pages or page_number < 1:
            raise Http404("page not found")

        page_obj = paginator.get_page(page_number)

        return render(request, 'news.html', {"news_list": page_obj})

    except (TypeError, AttributeError):
        raise Http404("page not found")


def news_detail(request, news_id):
    try:
        print(f'news id here {news_id}')
        news_raw = News.objects.get(pk=news_id)
        news_markdown = markdown.markdown(news_raw.content, extensions=['markdown.extensions.fenced_code'])
        return render(request, 'detail.html', {'news': news_markdown})
    except News.DoesNotExist:
        return HttpResponse("News not found.")


def project(request):
    return render(request, 'project.html')


def patents(request):
    return render(request, 'patents.html')


def writings(request):
    return render(request, 'writings.html')


def contactus(request):
    return render(request, 'contactus.html')
