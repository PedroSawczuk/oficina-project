from django.urls import *
from core.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="homePage"),

]
