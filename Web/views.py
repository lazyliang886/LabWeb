from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *
import markdown
import re


def test(request):
    return render(request, 'Web/test.html')


def home(request):
    img_list = IndexImgCarousel.objects.order_by("-upload_time")[:4]
    introduction = LabIntroduction.objects.all()
    if len(introduction) > 0:
        introduction = introduction[0]
    else:
        introduction = '暂时没有简介'

    lead_in = LabLeadIn.objects.all()
    if len(lead_in) > 0:
        lead_in = lead_in[0]
    else:
        lead_in = '暂时没有简介'

    LabProprietarySystem_list = LabProprietarySystem.objects.all()

    latest_news_list = News.objects.order_by("-pubdate")[:5]
    print(latest_news_list)

    return render(request, 'Web/home.html', {'img_list': img_list, 'introduction': introduction,
                                             'LabProprietarySystem_list': LabProprietarySystem_list,
                                             'latest_news_list': latest_news_list,
                                             'lead_in': lead_in})


def research_dir(request):
    return render(request, 'Web/research.html')


def handle_team_data(data_all):
    data_list = []
    data_temp = []

    for i in data_all:
        data_temp.append(i)
        if len(data_temp) == 4:
            data_list.append(data_temp)
            data_temp = []
    if len(data_temp) > 0:
        data_list.append(data_temp)

    return data_list


def team_t_s(request):
    teacher_list = handle_team_data(Teacher.objects.all())
    postgraduate_list = handle_team_data(Postgraduate.objects.all())
    undergraduate_list = handle_team_data(Undergraduate.objects.all())

    for i in teacher_list:
        for j in i:
            print(j)

    return render(request, 'Web/team_t_s.html',
                  {"teacher_list": teacher_list,
                   "postgraduate_list": postgraduate_list,
                   "undergraduate_list": undergraduate_list})


def thesis(request):
    return render(request, 'Web/thesis.html')


def personnel_training(request):
    return render(request, 'Web/train.html')


def news(request):
    news_list = News.objects.order_by("-pubdate")
    paginator = Paginator(news_list, 10)
    page_number_raw = request.GET.get("page")

    if not page_number_raw:
        page_obj = paginator.get_page(1)
        return render(request, 'Web/news.html', {"news_list": page_obj})

    try:
        page_number = re.match('\\d+', page_number_raw)
        page_number = int(page_number.group())

        if page_number > paginator.num_pages or page_number < 1:
            raise Http404("page not found")

        page_obj = paginator.get_page(page_number)

        return render(request, 'Web/news.html', {"news_list": page_obj})

    except (TypeError, AttributeError):
        raise Http404("page not found")


def news_detail(request, news_id):
    news_raw = get_object_or_404(News, pk=news_id)
    news_markdown = markdown.markdown(news_raw.content, extensions=['markdown.extensions.fenced_code'])
    return render(request, 'Web/detail.html', {'news': news_markdown})


def project(request):
    return render(request, 'Web/project.html')


def patents(request):
    return render(request, 'Web/patents.html')


def writings(request):
    return render(request, 'Web/writings.html')


def contactus(request):
    return render(request, 'Web/contactus.html')
