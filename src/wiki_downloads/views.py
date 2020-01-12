"""View module for wiki_downloads application"""
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .utils import wiki_api


def search_view(request):
    """
    This view performs the search operations on the api based on the given input
    :param request: Get request with search as query parameter input
    :return: returns the list matching the input string as a JSON response
    """
    if request.method == 'GET':
        context = {'data': list()}
        input = request.GET.get('search')
        if input:
            response = wiki_api.search_api(input)
            context = {'data': response.json()[1]}
        return JsonResponse(context)


def page_view(request):
    """
    This view fetches the content of the page based on the given input
    :param request: Get request with title as query parameter input
    :return: returns an HTML page
    """
    if request.method == 'GET':
        title = request.GET.get('title')
        template_name = 'page.html'
        file_content = wiki_api.page_api(title=title)
        f = open('./wiki_downloads/static/page_content.html', 'w+')
        f.write(file_content.text)
        f.close()
        context = {
            'file_name': 'page_content.html',
            'title': title
        }
        return render(request=request, template_name=template_name, context=context)


def page_download_view(request):
    """
    This view is to download the content of the page based on the given input
    :param request: Get request with title as query parameter input
    :return: returns a response in pdf format
    """
    if request.method == 'GET':
        title = request.GET.get('title')
        response = HttpResponse(wiki_api.page_api(title=title, output_format='pdf'))
        response['Content-Disposition'] = 'attachment; filename= %s.pdf' % title.replace(' ', '_')
        return response


