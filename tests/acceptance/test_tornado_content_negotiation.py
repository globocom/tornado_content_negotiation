# -*- coding: utf-8 -*-


from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application, asynchronous, RequestHandler

from tornado_content_negotiation import ContentNegotiation


class ContentNegotiationTestCase(AsyncHTTPTestCase):

    def test_should_return_content_type_header(self):
        self.http_client.fetch(self.get_url('/'), self.stop, headers={'Accept': 'application/json; q=0.9, text/html; q=0.8'})
        headers = self.wait().headers
        self.assertEqual(headers['Content-Type'], 'application/json; charset=UTF-8')

    def test_should_return_406_when_content_type_is_not_acceptable(self):
        self.http_client.fetch(self.get_url('/'), self.stop, headers={'Accept': 'text/plain'})
        code = self.wait().code
        self.assertEqual(code, 406)

    def get_app(self):
        return Application([(r'/', ContentNegotiationHandler)])


class ContentNegotiationHandler(ContentNegotiation, RequestHandler):

    def __init__(self, *args, **kwargs):
        content_types = ['application/json; charset=UTF-8', 'text/html; charset=UTF-8']
        super(ContentNegotiationHandler, self).__init__(negotiable_server_content_types=content_types, *args, **kwargs)

    @asynchronous
    def get(self):
        self.negotiated_mime_type()
        self.negotiated_content_type()
        self.set_negotiated_content_type_header()
        self.finish()
