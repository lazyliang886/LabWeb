from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe

# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin(request):
    error = ''
    if request.method == 'GET':
        return render(request, 'admin.html', {'error': error})
    # post检验账户是否正确，跳转后台管理
    account = request.POST.get("account")
    pwd = request.POST.get("password")
    # 开始检验 失败报错，成功跳转 django的MoudelForm检验，错误会传递给前端
    error = '输入的账号或密码错误'
    # 测试跳转
    if account == '123':
        if pwd == '123':
            return redirect('https://www.baidu.com/')   # 重定向后台界面
    return render(request, 'admin.html', {'error': error})


def research_dir(request):
    '''研究方向'''
    data = '123456\nasdfaf'  # 数据库读取
    if request.method == 'GET':
        return render(request, 'research.html',{'data':data})

def team_t_s(request):
    '''师生队伍'''
    data = '实验室成员组成：导师两名，研究生数名，本科生数名'   # 简要说明实验室的人员情况
    # 导师数据库表，id（自带希望从1开始） 名字 头像位置  职称（教授，导师助理）也可以给每个人排序 用序号计算
    # 测试研究生数据,可能需要更改
    tutor = []      # 导师列表
    queryset_tutor = []       # 获得数据库objects.all()
    for obj in queryset_tutor:
        row = obj.id/4  # 计算在第几行，从0行开始
        if obj.id % 4 == 1:
            temp = obj.name+'  '+obj.position
            str = '<div class="body31" style="margin-top : {}px;"> <div class="body311"> <img src="{}" alt="无法加载"> </div> ' \
                '<div class="body312" style="text-align: center;"> {}</div> </div>'.format(230*row+10,obj.image,temp)
            # 第一个设置外边距，第二个图片地址，第三个名字加介绍
        else:
            temp = obj.name + '  ' + obj.position
            str = '<div class="body42" style="margin-top : {}px;> <div class="body311"> <img src="{}" alt="无法加载"> </div> ' \
                  '<div class="body312" style="text-align: center"> {} </div> </div>'.format(230*row+10,obj.image,temp)
        tutor.append(str)

    # 研究生数据库表，id（自带希望从1开始） 名字 头像位置  入学年份（例2021级）
    postgraduate = []  # 研究生列表
    queryset_pg = []  # 获得数据库objects.all()
    for obj in queryset_pg:
        row = obj.id / 4  # 计算在第几行，从0行开始
        if obj.id % 4 == 1:
            temp = obj.name + '  ' + obj.position
            str = '<div class="body41" style="margin-top : {}px> <div class="body311"> <img src="{}" alt="无法加载"> </div> ' \
                  '<div class="body312" style="text-align: center"> {}</div> </div>'.format(230*row+10,obj.image,temp)
        else:
            temp = obj.name + '  ' + obj.position
            str = '<div class="body42" style="margin-top : {}px> <div class="body311"> <img src="{} alt="无法加载"> </div> ' \
                  '<div class="body312" style="text-align: center"> {} </div> </div>'.format(230*row+10,obj.image,temp)
        postgraduate.append(str)

    # 本科生数据库表，id（自带希望从1开始） 名字 头像位置  入学年份（例2021级）
    undergraduate = []  # 本科生列表
    queryset_ug = []  # 获得数据库objects.all()
    for obj in queryset_ug:
        row = obj.id / 4  # 计算在第几行，从0行开始
        if obj.id % 4 == 1:
            temp = obj.name + '  ' + obj.position
            str = '<div class="body41" style="margin-top : {}px> <div class="body311"> <img src="{}" alt="无法加载"> </div> ' \
                  '<div class="body312" style="text-align: center"> {}</div> </div>'.format(230*row+10,obj.image,
                                                                                                          temp)
        else:
            temp = obj.name + '  ' + obj.position
            str = '<div class="body42" style="margin-top : {}px> <div class="body311"> <img src="{} alt="无法加载"> </div> ' \
                  '<div class="body312" style="text-align: center"> {}</div> </div>'.format(230*row+10,obj.image,
                                                                                                          temp)
        undergraduate.append(str)

    if request.method == 'GET':
        return render(request, 'team_t_s.html', {'data': data,'tutor':tutor,'postgraduate':postgraduate,'undergraduate':undergraduate})

def thesis(request):
    '''论文'''
    # 将全部数据库的论文读取（需要格式一致）
    thesis = ['1\n', '2\n']  # 可以用列表存字符串或者列表里嵌套字典
    if request.method == 'GET':
        return render(request, 'thesis.html',{'thesis':thesis})

def personnel_training(request):
    '''人才培养'''
    # 将全部数据库的人才培养读取（需要格式一致）
    data = '12345'
    if request.method == 'GET':
        return render(request, 'train.html',{'data':data})

def news(request):
    '''新闻'''
    # 将全部数据库的新闻读取（需要格式一致）
    pages = 10   # 一页10条内容，判断数据库中内容有多少页（一页多少条可后面修改）
    # 智能分页https://zhuanlan.zhihu.com/p/90795230  https://zhuanlan.zhihu.com/p/367143925
    page = int(request.GET.get('page',1))
    page_size = 10
    start = (page - 1)*page_size
    end = page*page_size

    queryset = []   # 样例数据库.objects.all()[0:10]取全部里的前10 .objects.filter(id=#)[0:10]

    total_count = 10    # 样例数据库.objects.all().count()
    total_count_page,div = divmod(total_count,page_size)
    if div:
        total_count_page+=1

    # 计算前5页后5页
    plus = 5
    if total_count_page <= plus:
        start_page = 1
        end_page = total_count_page + 1
    else:
        if page <= plus:
            start_page = 1
            end_page = 2*plus + 1
        else:
            if (page + plus) > total_count_page:
                end_page = total_count_page
                start_page = total_count_page - 2 * plus
            else:
                start_page = page-plus
                end_page = page+plus+1
    page_str_list = []
    for i in range(start_page, end_page):
        if i == page:
            temp = '<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
        else:
            temp = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(temp)
    page_string = mark_safe("".join(page_str_list))
    if request.method == 'GET':
        news = []  # 获取当页内容,可以用列表存字符串或者列表里嵌套字典,存取要展示的信息
        # '< a href = "{}" >{}< / a >'.format(超链接对应地址,内容)
        return render(request, 'news.html', {'page_string': page_string,'news':news})


def project(request):
    '''项目'''
    # 将全部数据库的项目读取（需要格式一致）
    projects = ['1\n', '2\n']  # 可以用列表存字符串或者列表里嵌套字典
    if request.method == 'GET':
        return render(request, 'project.html', {'projects': projects})

def patents(request):
    '''专利'''
    # 将全部数据库的专利读取（需要格式一致）
    patents = ['1\n', '2\n']  # 可以用列表存字符串或者列表里嵌套字典
    if request.method == 'GET':
        return render(request, 'patents.html', {'patents': patents})

def writings(request):
    '''著作'''
    # 将全部数据库的著作读取（需要格式一致）
    writings = ['1\n','2\n']   #可以用列表存字符串或者列表里嵌套字典
    if request.method == 'GET':
        return render(request, 'writings.html',{'writings': writings})

def call_us(request):
    ''' 联系我们 '''
    #问题，文字需要格式，开头缩进，字体大小22px

    # 数据库读入或者写死，只有我们几个开发人员和实验室的联系方式（实验室的联系方式应该不会变）
    text = '\t 你好！\n welcome'
    return render(request, 'call_us.html', {'Text': text})