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
    
    def test_should_return_negotiated_content_type_when_matches_have_equal_weight(self):
        negotiated_content_type = self._content_negotiation_equal_weight().negotiated_content_type()
        self.assertEqual(negotiated_content_type, 'application/json; charset=UTF-8')
    
    def test_should_raise_error_on_invalid_arguments(self):
        self.assertRaises(ValueError, ContentNegotiation)
    
    def _content_negotiation(self):
        content_types = ['application/json; charset=UTF-8', 'text/html; charset=UTF-8']
        content_negotiation = ContentNegotiation(negotiable_server_content_types=content_types)
        content_negotiation.request = MagicMock()
        content_negotiation.request.headers.get = MagicMock(return_value='application/json; q=0.9, text/html; q=0.8')
        return content_negotiation
    
    def _content_negotiation_equal_weight(self):
        content_types = ['application/json; charset=UTF-8', 'text/html; charset=UTF-8']
        content_negotiation = ContentNegotiation(negotiable_server_content_types=content_types)
        content_negotiation.request = MagicMock()
        content_negotiation.request.headers.get = MagicMock(return_value='application/json, text/html')
        return content_negotiation
