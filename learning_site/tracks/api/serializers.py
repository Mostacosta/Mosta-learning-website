from rest_framework import serializers
from ..models import track as track_,course as course_,lesson,exam,exam_result
from contacts.api.serializers import user_serializer


class track_serializer (serializers.ModelSerializer):
    class Meta :
        model = track_
        fields = '__all__'

class course_serializer (serializers.ModelSerializer):
    track = track_serializer(many=True)
    succeeded_users = user_serializer(many=True)
    class Meta :
        model = course_
        fields = '__all__'

class lesson_serializer (serializers.ModelSerializer):
    course = course_serializer()
    watching_users = user_serializer(many=True)
    class Meta :
        model = lesson
        fields = '__all__'

class exam_serializer (serializers.ModelSerializer):
    class Meta :
        model = exam
        fields = ('name','question','answer1','answer2','answer3','answer4','right_answer')
        read_only_fields = ('question','answer1','answer2','answer3','answer4')
        extra_kwargs = {
            'right_answer': {'write_only': True,'required': True},
        }


class exam_result_serializer (serializers.ModelSerializer):
    course = course_serializer()
    user = user_serializer()
    class Meta :
        model = exam_result
        fields = '__all__'