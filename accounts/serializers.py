
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data.pop('refresh', None) # remove refresh from the payload
#         data['access'] = str(refresh.access_token)

#         # Add extra responses here
#         data['role'] = self.user.role
#         return data

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

     def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['role'] = self.user.role
        data['id'] = self.user.id
        return data