# drf-tracking-extended

[![Build Status](https://travis-ci.org/frankie567/drf-tracking.svg?branch=drf-tracking-extended)](https://travis-ci.org/frankie567/drf-tracking)
[![PyPI version](https://badge.fury.io/py/drf-tracking-extended.svg)](https://badge.fury.io/py/drf-tracking-extended)
[![Requirements Status](https://requires.io/github/frankie567/drf-tracking/requirements.svg?branch=drf-tracking-extended)](https://requires.io/github/frankie567/drf-tracking/requirements/?branch=drf-tracking-extended)

## Overview

drf-tracking-extended is a fork of [drf-tracking](https://github.com/aschn/drf-tracking) providing a Django model and DRF view mixin that work together to log Django Rest Framework requests to the database. You'll get these attributes for every request/response cycle to a view that uses the mixin:

 Model field name | Description | Model field type
------------------|-------------|-----------------
`user` | User if authenticated, None if not | Foreign Key
`requested_at` | Date-time that the request was made | DateTimeField
`response_ms` | Number of milliseconds spent in view code | PositiveIntegerField
`path` | Target URI of the request, e.g., `"/api/"` | CharField
`view` | Target VIEW of the request, e.g., `"views.api.ApiView"` | CharField
`view_method` | Target METHOD of the VIEW of the request, e.g., `"get"` | CharField
`remote_addr` | IP address where the request originated (X_FORWARDED_FOR if available, REMOTE_ADDR if not), e.g., `"127.0.0.1"` | GenericIPAddressField
`host` | Originating host of the request, e.g., `"example.com"` | URLField
`authentication` | Authentication class used to authenticate user, None if no user authenticated, e.g. `"rest_framework.authentication.TokenAuthentication"` | CharField
`method` | HTTP method, e.g., `"GET"` | CharField
`query_params` | Dictionary of request query parameters, as text | TextField
`data` | Dictionary of POST data (JSON or form), as text | TextField
`response` | JSON response data | TextField
`status_code` | HTTP status code, e.g., `200` or `404` | PositiveIntegerField


## Requirements

* Django 1.8, 1.9, 1.10, 1.11
* Django REST Framework and Python release supporting the version of Django you are using

## Installation

Install using `pip`...

```bash
$ pip install drf-tracking-extended
```

Register with your Django project by adding `rest_framework_tracking`
to the `INSTALLED_APPS` list in your project's `settings.py` file.
Then run the migrations for the `APIRequestLog` model:

```bash
$ python manage.py migrate
```

## Usage

Add the `rest_framework_tracking.mixins.LoggingMixin` to any DRF view
to create an instance of `APIRequestLog` every time the view is called.

For instance:
```python
# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin

class LoggingView(LoggingMixin, generics.GenericAPIView):
    def get(self, request):
        return Response('with logging')
```

For performance enhancement, explicitly choose methods to be logged using `logging_methods` attribute:
```python
class LoggingView(LoggingMixin, generics.CreateModelMixin, generics.GenericAPIView):
    logging_methods = ['POST', 'PUT']
    model = ...
```

If you don't want to save JSON response data in database, set the `logging_save_response` attribute to `False`:
```python
class LoggingView(LoggingMixin, generics.CreateModelMixin, generics.GenericAPIView):
    logging_save_response = False
    model = ...
```

You can provide a more advanced logic to determine if the request should be logged or not by overriding `_should_log_request` method. By default, check if the method is in `logging_methods`. Example:
```python
class LoggingView(LoggingMixin, generics.CreateModelMixin, generics.GenericAPIView):
    def _should_log_request(self, request):
        """
        Ignore requests made from localhost
        """
        return request.META.get('REMOTE_ADDR') != 'localhost'
```

You can provide a more advanced logic to determine if the response should be logged or not by overriding `_should_log_response` method. By default, always `True`. Example:
```python
class LoggingView(LoggingMixin, generics.CreateModelMixin, generics.GenericAPIView):
    def _should_log_response(self, response):
        """
        Log only errors
        """
        return response.status_code >= 400
```

Obviously, for a request to be logged, both `_should_log_request` and `_should_log_response` should resolve to `True`.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```
