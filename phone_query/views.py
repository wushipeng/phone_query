from django.shortcuts import render, HttpResponse
from phone_query import models
from django.views import View
from django.db.models import Q
import xlrd
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.


class Index(View):
    """首页"""
    def __init__(self, **kwargs):
        super(Index, self).__init__(**kwargs)
        self.obj_this_hidden = models.PersonPhone.objects.all().values("name", "phone_number", "part")
        self.t_title = []
        for i in models.PersonPhone._meta.get_fields():
            if i.__dict__["verbose_name"] == "ID" or i.__dict__["verbose_name"] == "员工姓名简称":
                pass
            else:
                self.t_title.append(i.__dict__["verbose_name"])

                self.obj_other = models.RegionalPhone.objects.values("city_name", "phone_number")
                self.obj_part_old = models.PersonPhone.objects.values("part")
                self.obj_part = set([i['part'] for i in self.obj_part_old])

    def get(self, request):

        obj_this = models.PersonPhone.objects.values("name","phone_number","part")
        tdata = self.page(request)
        return render(request, "index.html",
                      {"t_title": self.t_title, "telnumber": tdata,
                       "telnumber_hidden": self.obj_this_hidden,
                       "citynumber": self.obj_other, "obj_part": self.obj_part,"tdata": tdata})

    def post(self, request):

        file = request.FILES.get("file")
        if file:
            try:
                wb = xlrd.open_workbook(
                    filename=file, file_contents=request.FILES['file'].read())  # 读取浏览器传过来的文件
            except Exception:
                return HttpResponse("上传的excel数据有误,请按照浏览器表格内的数据格式进行Excel整理")

            table = wb.sheets()[0]
            row = table.nrows
            for i in range(1, row):
                col = table.row_values(i)

                models.PersonPhone.objects.create(
                    name=col[0], pyjc=col[1], phone_number=int(col[2]), part=col[3])
       
        result = request.POST.get("crid")
        select = request.POST.get("select_part")
        if not result:
            obj_this = models.PersonPhone.objects.all().values("name", "phone_number", "part")
        else:
            obj_this = models.PersonPhone.objects.filter(Q(name__icontains=result) | Q(pyjc__icontains=result)).values("name", "phone_number", "part")

        return render(request, "index.html",
                      {"t_title": self.t_title, "telnumber": obj_this,"telnumber_hidden": self.obj_this_hidden, "citynumber": self.obj_other, "obj_part": self.obj_part})

    def page(self,request):
        """分页查询"""
        page = request.GET.get("page")

        tdata = models.PersonPhone.objects.all().values("name", "phone_number", "part")

        paginator = Paginator(tdata, 5)  # 每页多少条数据

        try:
            tdata = paginator.page(page)  # 返回 page（页数）的数据

        except PageNotAnInteger:
            tdata = paginator.page(1)  # 第一页

        except EmptyPage:
            tdata = paginator.page(paginator.num_pages)  # 最后一页

        return tdata

    @staticmethod
    def not_found(request):
        """404页面"""
        return render(request, "404.html")





