from rest_framework import viewsets
from rest_framework import response
from rest_framework import status
from email_validator import validate_email
from email_validator import EmailNotValidError

from . import functions

# Create your views here.


class EmailViewSet(viewsets.ViewSet):
    """
    To send email to the user requested in the parameters
    """

    def create(self, request):
        to = request.data.get('to')
        if not to:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'To is required'})
        try:
            to = validate_email(to)
            to = to['email']
        except EmailNotValidError:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'To email is not valid'})
        to_name = request.data.get('to_name')
        if not to_name:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'to_name is required'})
        from_user = request.data.get('from')
        if not from_user:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'from is required'})
        try:
            from_user = validate_email(from_user)
            from_user = from_user['email']
        except EmailNotValidError:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'From email is not valid'})
        from_name = request.data.get('from_name')
        if not from_name:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'from_name is required'})
        subject = request.data.get('subject')
        if not subject:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'subject is required'})
        body = request.data.get('body')
        if not body:
            return response.Response(status=status.HTTP_400_BAD_REQUEST,
                                     data={'body is required'})

        email_response = functions.send_simple_message(to, from_user,
                                                       subject, body)
        print(email_response.__dict__)
        return response.Response(status=email_response.status_code)
