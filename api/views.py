from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class PingView(APIView):
    def get(self, request, format=None):
        """
        Return 'pong' if it worked.
        """
        return Response({"status": "pong"})
