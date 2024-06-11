from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def _paginator(request, query_set, num_per_page=15):
    page = request.GET.get('page', 1)
    paginator = Paginator(query_set, num_per_page)
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)
    return query_set