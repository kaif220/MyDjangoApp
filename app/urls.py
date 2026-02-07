from .views import rendersomething,Aboutsomething
from django.urls import path
urlpatterns = [
    
    path("",rendersomething,name="render"),
    path("about",Aboutsomething,name="about")
]
