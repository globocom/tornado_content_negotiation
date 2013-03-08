# -*- coding: utf-8 -*-


from unittest import TestCase

from mock import MagicMock

from tornado_content_negotiation import ContentNegotiation


class ContentNegotiationTestCase(TestCase):
    
    def test_should_return_negotiated_content_type(self):
        negotiated_content_type = self._content_negotiation().negotiated_content_type()
        self.assertEqual(negotiated_content_type, 'application/json; charset=UTF-8')
    
    def test_should_return_negotiated_mime_type(self):
        negotiated_mime_type = self._content_negotiation().negotiated_mime_type()
        self.assertEqual(negotiated_mime_type, 'application/json')
    
    def test_should_not_ignore_wildcard_in_negotiable_server_content_types(self):
        negotiated_content_type = self._content_negotiation_with_wildcard().negotiated_content_type()
        self.assertEqual(negotiated_content_type, 'application/json; charset=UTF-8')
    
    def test_should_raise_error_on_invalid_arguments(self):
        self.assertRaises(ValueError, ContentNegotiation)

    def _content_negotiation(self):
        content_negotiation = ContentNegotiation(negotiable_server_content_types=['application/json; charset=UTF-8'])
        content_negotiation.request = MagicMock()
        content_negotiation.request.headers.get = MagicMock(return_value='application/json')
        return content_negotiation

    def _content_negotiation_with_wildcard(self):
        content_negotiation = ContentNegotiation(negotiable_server_content_types=['application/json; charset=UTF-8'])
        content_negotiation.request = MagicMock()
        content_negotiation.request.headers.get = MagicMock(return_value='*/*')
        return content_negotiation
