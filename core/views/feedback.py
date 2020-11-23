from django.conf import settings

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .. import tasks
from ..permissions import IsVerified
from ..serializers.feedback import FeedbackSerializer


class FeedbackView(APIView):
    permission_classes = (IsAuthenticated, IsVerified)

    def post(self, request):
        fs = FeedbackSerializer(data=request.data)

        if fs.is_valid():
            tasks.send_mail.delay(fs.validated_data['subject'],
                                  fs.validated_data['message'],
                                  request.user.email,
                                  (settings.FEEDBACK_EMAIL,))
            return Response(status=status.HTTP_202_ACCEPTED, data=fs.errors)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=fs.errors)
