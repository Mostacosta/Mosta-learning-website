from rest_framework.serializers import ModelSerializer
from tracks.api.serializers import lesson_serializer
from contacts.api.serializers import user_serializer
from ..models import question,answer

class question_serializer (ModelSerializer):
    lesson = lesson_serializer(required=False)
    user = user_serializer(required=False)
    class Meta:
        model = question
        fields = '__all__'

class answer_serializer (ModelSerializer):
    question = question_serializer(required=False)
    user = user_serializer(required=False)
    likes = user_serializer(many=True,required=False)
    class Meta :
        model = answer
        fields = '__all__'
