mozilla-cloud-services-logger
-----------------------------

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

Testing
=======
```python
pip install jsonschema testfixtures
python tests.py
```
