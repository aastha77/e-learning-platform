from django.contrib import admin
from .models import User, Course, Enrollment, Quiz, Question, Answer, StudentAnswer

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudentAnswer)
