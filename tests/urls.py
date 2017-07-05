# coding=utf-8
from __future__ import absolute_import

from django.conf.urls import url

from . import views as test_views

urlpatterns = [
    url(r'^no-logging$', test_views.MockNoLoggingView.as_view()),
    url(r'^logging$', test_views.MockLoggingView.as_view()),
    url(r'^slow-logging$', test_views.MockSlowLoggingView.as_view()),
    url(r'^explicit-logging$', test_views.MockExplicitLoggingView.as_view()),
    url(r'^no-response-save-logging$', test_views.MockNotSaveResponseLoggingView.as_view()),
    url(r'^session-auth-logging$', test_views.MockSessionAuthLoggingView.as_view()),
    url(r'^token-auth-logging$', test_views.MockTokenAuthLoggingView.as_view()),
    url(r'^json-logging$', test_views.MockJSONLoggingView.as_view()),
    url(r'^validation-error-logging$', test_views.MockValidationErrorLoggingView.as_view()),
    url(r'^404-error-logging$', test_views.Mock404ErrorLoggingView.as_view()),
    url(r'^500-error-logging$', test_views.Mock500ErrorLoggingView.as_view()),
    url(r'^415-error-logging$', test_views.Mock415ErrorLoggingView.as_view()),
    url(r'^only-error-logging$', test_views.MockOnlyErrorLoggingView.as_view()),
    url(r'^no-view-log$', test_views.MockNameAPIView.as_view()),
    url(r'^view-log$', test_views.MockNameViewSet.as_view({'get': 'list'})),
    url(r'^400-body-parse-error-logging$', test_views.Mock400BodyParseErrorLoggingView.as_view()),
]
