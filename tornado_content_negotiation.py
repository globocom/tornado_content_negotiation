# -*- coding: utf-8 -*-


import mimeparse
from tornado.web import HTTPError


class ContentNegotiation(object):
    
    def __init__(self, *args, **kwargs):
        self._negotiable_server_content_types = kwargs.pop('negotiable_server_content_types', None)
        if not self._negotiable_server_content_types:
            raise ValueError('You need to set negotiable_server_content_types for content negotiation to work.')
        self._negotiable_server_content_types = reversed(self._negotiable_server_content_types)
        super(ContentNegotiation, self).__init__(*args, **kwargs)
    
    def set_negotiated_content_type_header(self):
        self.set_header('Content-Type', self.negotiated_content_type())
    
    def negotiated_content_type(self):
        return self._negotiate_content_type()
    
    def negotiated_mime_type(self):
        parsed_mime_type = mimeparse.parse_mime_type(self._negotiate_content_type())
        return '%s/%s' % (parsed_mime_type[0], parsed_mime_type[1])
    
    def _negotiate_content_type(self):
        if not hasattr(self, '_negotiated_content_type'):
            accept = self.request.headers.get('Accept')
            self._negotiated_content_type = mimeparse.best_match(self._negotiable_server_content_types, accept)
            if not self._negotiated_content_type:
                self.set_status(406)
                if not self._finished:
                    self.finish()
        return self._negotiated_content_type
