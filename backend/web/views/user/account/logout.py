from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]#用户必须登录才能访问此视图

    def post(self, request):
        try:
            response = Response({"result": "success"})
            response.delete_cookie('refresh_token')
            return response
        except:
            return Response({"result": "系统异常，请稍后重试"})