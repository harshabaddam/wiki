"""Python wrapper for Wikipedia's APIs"""
import requests


def search_api(search, url='https://en.wikipedia.org/w/api.php', action='opensearch', output_format='json', limit=20):
    """
    This is a wrapper for performing the get request on the api for search based on input string
    :param search: input string
    :param url: URL of the Wikipedia's API
    :param action: type of action to be performed on api
    :param output_format: specify the output format of the response object
    :return: returns the response object of get request
    """
    payload = {
        'action': action,
        'format': output_format,
        'search': search,
        'limit': limit
    }
    return requests.get(url=url, params=payload)


def page_api(title, url='https://en.wikipedia.org/api/rest_v1/page', output_format='html'):
    """
    This is a wrapper for fetching the content of the page
    :param title: input string as title of the page
    :param url: URL for fetching the page content
    :param output_format: specify the output format of the response object
    :return: returns the responds object of get request
    """
    url = '%s/%s/%s' % (url, output_format, title)
    return requests.get(url=url)


if __name__ == '__main__':
    search_api()

