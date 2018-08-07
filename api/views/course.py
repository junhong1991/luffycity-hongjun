from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from api import models
from api.serializers.course import CourseSerializer
from rest_framework.pagination import PageNumberPagination
from api.serializers.course import CourseSerializer, CourseModelSerializer, CourseSpecialModelSerializer
from api.utils.response import BaseResponse


class CoursesView(APIView):

    def get(self,request,*args,**kwargs):
        # response = {'code':1000,'data':None,'error':None}
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            ser = CourseModelSerializer(instance=course_list,many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)


class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)


class CoursesSpecialView(APIView):
    """展示所有的专题课"""
    def get(self, request,  *args, **kwargs):
        ret = BaseResponse()
        queryset = models.Course.objects.filter(degree_course__isnull=True)
        ser = CourseSpecialModelSerializer(instance=queryset, many=True)
        ret.data = ser.data
        return Response(ret.dict)
