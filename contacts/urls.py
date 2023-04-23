from django.urls import path

from contacts.views import ContactView, sendMail, SizingView

app_name = 'contacts'

urlpatterns = [
    path('', ContactView.as_view(), name='contact-page'),
    path('sizing/', SizingView.as_view(), name='sizing-page'),
    path('api/mail', sendMail, name='sendmail'),
]