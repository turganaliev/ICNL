import datetime
import random
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User, Code
from users.serializers import CodeSerializer


def get_code():
    return str(random.randint(100000, 999999))


class RegisterView(APIView):
    def post(self, request):
        phone = request.data.get('username')
        new_user = User.objects.create(username=phone)
        new_user.is_active = True
        new_user.save()
        code = get_code()
        code = Code.objects.create(conf_code=code, valid_until=datetime.datetime.now() +
                                   datetime.timedelta(minutes=24),
                                   user=new_user)

        code.save()
        return Response(status=status.HTTP_200_OK, data=CodeSerializer(code).data)


class ConfirmAPIView(APIView):
    def post(self, request):
        code = request.data.get('conf_code')
        confirmations = Code.objects.filter(conf_code=code, valid_until__gte=datetime.datetime.now())
        if not confirmations:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Невалидный код'})
        else:
            token = None
            try:
                token = Token.objects.get(user=confirmations[0].user)
                print('GET TOKEN')
            except:
                pass
            if token is None:
                token = Token.objects.create(user=confirmations[0].user)
                token.save()
                print('CREATE TOKEN')
        return Response(status=status.HTTP_200_OK, data={'key': token.key})