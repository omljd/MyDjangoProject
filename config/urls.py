from django.contrib import admin
from django.urls import include, path
from employees.views import EmployeeListView

urlpatterns = [
    path("", EmployeeListView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("employees/", include("employees.urls", namespace="employees")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
]

