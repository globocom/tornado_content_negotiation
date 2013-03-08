# -*- coding: utf-8 -*-


from tornado.web import HTTPError

from httpheader import acceptable_content_type


class ContentNegotiation(object):
    
    def __init__(self, *args, **kwargs):
        self._negotiable_server_content_types = kwargs.pop('negotiable_server_content_types', None)
        if not self._negotiable_server_content_types:
            raise ValueError('You need to set negotiable_server_content_types for content negotiation to work.')
        super(ContentNegotiation, self).__init__(*args, **kwargs)
    
    def set_negotiated_content_type_header(self):
        self.set_header('Content-Type', self.negotiated_content_type())
    
    def negotiated_content_type(self):
        return str(self._negotiate_content_type())
    
    def negotiated_mime_type(self):
        return self._negotiate_content_type().media_type
    
    def _negotiate_content_type(self):
        if not hasattr(self, '_negotiated_content_type'):
            accept = self.request.headers.get('Accept')
            content_type = acceptable_content_type(
                accept,
                self._negotiable_server_content_types,
                ignore_wildcard=False
            )
            if not content_type:
                self.set_status(406)
                if not self._finished:
                    self.finish()
            self._negotiated_content_type = content_type[0]
        return self._negotiated_content_type
