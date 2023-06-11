from django.urls import path


from .views import LoginForm


urlpatterns = [
    path('', LoginForm.as_view()),
]
