from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # api
    url(r'^api/customer/$', views.CustomerViews.as_view()),
    url(r'^api/payM/$', views.PaymentView.as_view()),
    url(r'^api/subscription/$', views.SubscriptionView.as_view()),
    url(r'^api/verification/$', views.VerificationView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
