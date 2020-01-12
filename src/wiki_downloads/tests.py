from django.test import TestCase
from django.urls import reverse


class WikiSearchViewTests(TestCase):

    def test_status_code(self):
        """
        Test case to check the status code of the search_view for input
        :return:
        """
        url = reverse('search')
        response = self.client.get(url, {'search': 'hello'})
        self.assertEqual(response.status_code, 200)

    def test_view_name(self):
        """
        Test case to check the correctness of the view name referred by the URL of the search_view
        :return:
        """
        url = reverse('search')
        response = self.client.get(url, {'search': 'hello'})
        self.assertEqual(response.resolver_match.func.__name__, 'search_view')

    def test_content_type(self):
        """
        Test case to check the content type of response is JSON
        :return:
        """
        url = reverse('search')
        response = self.client.get(url, {'search': 'hello'})
        self.assertEqual(response['Content-Type'], 'application/json')


class WikiPageViewTests(TestCase):

    def test_status_code(self):
        """
        Test case to check the status code of the page_view for input
        :return:
        """
        url = reverse('page')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response.status_code, 200)

    def test_view_name(self):
        """
        Test case to check the correctness of the view name referred by the URL of the page_view
        :return:
        """
        url = reverse('page')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response.resolver_match.func.__name__, 'page_view')

    def test_content_type(self):
        """
        Test case to check the content type of response is html
        :return:
        """
        url = reverse('page')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')


class WikiPageDownloadViewTests(TestCase):

    def test_status_code(self):
        """
        Test case to check the status code of the page_download_view for input
        :return:
        """
        url = reverse('download')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response.status_code, 200)

    def test_view_name(self):
        """
        Test case to check the correctness of the view name referred by the URL of the page_download_view
        :return:
        """
        url = reverse('download')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response.resolver_match.func.__name__, 'page_download_view')

    def test_content_type(self):
        """
        Test case to check the content type of response is html
        :return:
        """
        url = reverse('download')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

    def test_content_disposition(self):
        """
        Test case to check the content disposition of response is attachment
        :return:
        """
        url = reverse('download')
        response = self.client.get(url, {'title': 'hello'})
        self.assertEqual(response['Content-Disposition'], 'attachment; filename= hello.pdf')
