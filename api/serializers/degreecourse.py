from rest_framework import serializers
from api import models


class DegreeCourseTeacherModelSerializer(serializers.ModelSerializer):
    """查看所有学位课以及学位课的授课老师"""
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['name', 'teachers']

    def get_teachers(self, row):
        teachers_list = row.teachers.all()
        return [{'id': item.id, 'name': item.name} for item in teachers_list]


class DegreeCourseScholarshipModelSerializer(serializers.ModelSerializer):
    """查看所有学位课名称以及学位课的奖学金"""
    scholarship = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['name', 'scholarship']

    def get_scholarship(self, row):
        scholarships = row.scholarship_set.all()
        return [{'id': item.time_percent, 'scholarships': item.value} for item in scholarships]
