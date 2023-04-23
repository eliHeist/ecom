from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView

from rest_framework.decorators import api_view
from rest_framework.response import Response

from contacts.models import Receipient


@api_view(['POST'])
def sendMail(request):
   if request.method == 'POST':
      data = request.data

      # get form data
      reason = data.get('reason')
      message = f'''
         Name: {data.get('name')}
         \nEmail: {data.get('email')}
         \nPhone: {data.get('phone')}
         \n\n\n{data.get('message')}
      '''
      # emails to send message to
      receipients = Receipient.objects.all()

      try:
         send_mail(
            subject=reason,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receipient.email for receipient in receipients]
         )

         return Response('SUCCESS')
      except Exception as e:
         print(f'Exception: {e}')
         return Response('Failed')


class ContactView(TemplateView):
   template_name = "contacts/contact-page.html"


class SizingView(TemplateView):
   template_name = "contacts/sizing-page.html"