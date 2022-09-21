from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer


class ProfileList(APIView):
    def get(self, request):
        Profiles=profile.objects.all()
        serializer=ProfileSerializer(Profiles, many=True)
        return Response(serializer.data)