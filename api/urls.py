from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("employees/",views.employeeviewsetview,basename="employee")
for u in router.urls:
    print("======",u,"========")
urlpatterns=[

]+router.urls

