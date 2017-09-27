# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Record
from .forms import RecordSearchForm


def Index(request):
    sort = request.GET.get('sort', 'artist')
    search = request.GET.get('search')
    search_by = request.GET.get('search_by')

    if request.method == 'POST':
        form = RecordSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            search_by = form.cleaned_data['search_by']
    else:
        form = RecordSearchForm(initial={'search': search, 'search_by': search_by})


    if search and search_by:
        if search_by == 'artist':
            all_records = Record.objects.filter(artist__icontains=search)
        elif search_by == 'title':
            all_records = Record.objects.filter(title__icontains=search)
        elif search_by == 'label':
            all_records = Record.objects.filter(label__icontains=search)
        else:
            all_records = Record.objects.filter(catalog_no__icontains=search)
    else:
        all_records = Record.objects.all()

    all_records = all_records.order_by(sort)

    paginator = Paginator(all_records, 20)
    page = request.GET.get('page', 1)
    page_int = int(page)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    if paginator.num_pages >= 13:
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
        page_range = range(1,paginator.num_pages)

    return render(request, 'records/index.html', {'records': records, 'page_range': page_range, 'sort' : sort, 'page' : page, 'form' : form, 'search' : search, 'search_by' : search_by})


def Show(request, pk, slug):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'records/show.html', { 'record': record })


def Api(request):
    sort = request.GET.get('sort', 'label')
    artist = request.GET.get('artist', None)
    title = request.GET.get('title', None)
    label = request.GET.get('label', None)
    catalog_no = request.GET.get('catalog_no', None)

    records = Record.objects.all()

    if artist:
        records = records.filter(artist__icontains=artist)
    if title:
        records = records.filter(title__icontains=title)
    if label:
        records = records.filter(label__icontains=label)
    if catalog_no:
        records = records.filter(catalog_no__icontains=catalog_no)

    records = records.order_by(sort).values('id','title', 'artist', 'label', 'catalog_no', 'discogs', 'thumb')
    record_list = list(records)

    if len(record_list):
        return JsonResponse(record_list, safe=False)
    else:
        records = { "message" : "no matching records found" }
        return JsonResponse(records, status=404)
