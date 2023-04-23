from django.urls import path

from mainfront.views import AboutPageView, ContactPageView, HomepageView

app_name = 'main'

urlpatterns = [
   path('', HomepageView.as_view(), name='home-page'),
   path('about/', AboutPageView.as_view(), name='about-page'),
]