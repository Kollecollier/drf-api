from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile


class ProfileList(APIView):
    def get(self, request):
        Profiles=profile.objects.all()
        return Response(profiles)