from django.urls import path, include
from ourcalendar import views


app_name = 'ourcalendar'

urlpatterns = [
    path("", views.TemplateView.as_view(), name="template"),
    path("share/", views.TemplateQR.as_view(), name='share'),
    path("addEvent/", views.create_event, name="newEvent"),
    path('account/',include('users.urls', namespace="users")),
    path('mergeCalendar/<int:id>',views.MergeCalendar.as_view(), name="template"),
    path("mergedCalendar/", views.MergeCalendar.as_view(), name="newEvent")
]