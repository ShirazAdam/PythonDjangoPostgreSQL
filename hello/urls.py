
from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    # remove .using('postgresql') to use default database
    queryset=LogMessage.objects.using('postgresql').order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    # path("", views.home, name="home"),
    # Replace the existing path for ""
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]