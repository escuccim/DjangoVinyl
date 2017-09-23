# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Record

# Create your views here.
def Index(request):
    sort = request.GET.get('sort','artist')

    all_records = Record.objects.all().order_by(sort)

    paginator = Paginator(all_records, 20)
    page = request.GET.get('page', 1)
    page_int = int(page)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    if all_records.count >= 13:
        if page_int >= 7 and page_int <= paginator.num_pages - 7:
            page_range = range(1,3)
            page_range = page_range + ['...']
            page_range = page_range + range(page_int-3, page_int+3)
            page_range = page_range + ['...']
            page_range = page_range + range(paginator.num_pages-1,paginator.num_pages+1)
        elif page_int >= records.paginator.num_pages - 7:
            page_range = range(1, 3)
            page_range = page_range + ['...']
            page_range = page_range + range(paginator.num_pages - 7, paginator.num_pages)
        else:
            page_range = range(1,8)
            page_range = page_range + ['...']
            page_range = page_range + range(paginator.num_pages - 1, paginator.num_pages + 1)
    else:
        page_range = range(1,all_records.count)


    return render(request, 'records/index.html', {'records': records, 'page_range': page_range, 'sort' : sort, 'page' : page})