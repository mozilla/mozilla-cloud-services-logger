mozilla-cloud-services-logger
-----------------------------

**Deprecated / Unmaintained** - This project is no longer maintained. Consider using [mozilla-services/python-dockerflow](https://github.com/mozilla-services/python-dockerflow) instead.

[![Build Status](https://travis-ci.org/mozilla/mozilla-cloud-services-logger.svg?branch=master)](https://travis-ci.org/mozilla/mozilla-cloud-services-logger)

This package provides two things:

1. `mozilla_cloud_services_logger.formatters.JsonLogFormatter`: [a Python
   logging Formatter][formatter] that produces messages following [the JSON
   schema for a common application logging format][mozlog] defined by Mozilla
   Cloud Services.

2. `mozilla_cloud_services_logger.django.middleware.RequestSummaryLogger`:
   [Django middleware][middleware] that emits the [`request.summary`][requestsummary]
   log event on every request.

[formatter]: https://docs.python.org/3/library/logging.html#formatter-objects
[mozlog]: https://github.com/mozilla-services/Dockerflow/blob/master/docs/mozlog.md
[middleware]: https://docs.djangoproject.com/en/1.8/topics/http/middleware/
[requestsummary]: https://github.com/mozilla-services/Dockerflow/blob/master/docs/mozlog.md#application-request-summary-type-requestsummary

## Examples

Django `settings.py`:

```python
MIDDLEWARE_CLASSES = (
    # ...
    'mozilla_cloud_services_logger.django.middleware.RequestSummaryLogger',
    # ...
)

LOGGING = {
    'version': 1,
    'formatters': {
        'json': {
            '()': 'mozilla_cloud_services_logger.formatters.JsonLogFormatter',
            'logger_name': 'MySiteName'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        },
    },
    'loggers': {
        'request.summary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
```

## Testing

```python
pip install jsonschema testfixtures
python tests.py
```
