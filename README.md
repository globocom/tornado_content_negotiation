# Tornado Content Negotiation [![Build Status](https://travis-ci.org/globocom/tornado_content_negotiation.png?branch=master)](https://travis-ci.org/globocom/tornado_content_negotiation)

Content Negotiation module for Tornado.

## Installing

```
pip install tornado_content_negotiation
```

## Using

Content Negotiation works by determining the best match content type based on the request's Accept header and the content types that your server is able to generate.

Add the ContentNegotiation mixin to your handler and define the content types your server is able to generate:

```
class HandlerWithContentNegotiation(ContentNegotiation, RequestHandler):
	
	def __init__(self, *args, **kwargs):
        content_types = ['application/json; charset=UTF-8', 'text/html; charset=UTF-8']
        super(ContentNegotiationHandler, self).__init__(negotiable_server_content_types=content_types,
        												*args,
        												**kwargs)
```

Set response's content type with the best match:

```
self.set_negotiated_content_type_header() # Content-Type: application/json; charset=UTF-8
```

Return best match content type:

```
self.negotiated_content_type() # application/json; charset=UTF-8
```

Return best match mime type:

```
self.negotiated_mime_type() # application/json
```

## Dependency

Tornado Content Negotiation depends on the httpheader.py by Deron Meranda for the actual parsing of the Accept HTTP Header. For more information, see:

- http://deron.meranda.us/python/httpheader
- https://github.com/dmeranda/httpheader

For convenience, this module is included here.

## License

Tornado Content Negotiation is licensed under the MIT License:

The MIT License

Copyright (c) 2013 globo.com

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
