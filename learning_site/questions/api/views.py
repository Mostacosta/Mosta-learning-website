from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import answer_serializer,question_serializer
from ..models import answer,question
from tracks.models import lesson

class questions_views (APIView):

    def get(self, request,format=None):
        q = request.GET.get("q",None)
        if q :
            answers = []
            lesson_ = lesson.objects.get(name=q)
            questions = question.objects.filter(lesson=lesson_)
            for question_ in questions:
                answers_ = answer.objects.filter(question=question_)
                if answers_:
                    serializer=answer_serializer(answers_,many=True)
                    answers.append(serializer.data)
            return Response (answers)
        return Response ("mfesh 7aga ")

    def post (self, request,format=None):
        data = request.data
        if "the_answer" in data:
            serializer = answer_serializer(data=data)
            if serializer.is_valid():
                question_ = question.objects.get(id=int(data["question"]))
                serializer.save(user=request.user,question=question_)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            serializer = question_serializer(data=data)
            if serializer.is_valid():
                lesson_ = lesson.objects.get(id=int(data["lesson_id"]))
                serializer.save(user=request.user,lesson=lesson_)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    def put (self, request,format=None):
        data = request.data
        answer_ = answer.objects.get(pk=int(data["answer_id"]))
        user = request.user
        if user in answer_.likes.all() :
                answer_.likes.remove(user)
        else:
                answer_.likes.add(user)
        serializer = answer_serializer(answer_)
        return Response(serializer.data)


    




