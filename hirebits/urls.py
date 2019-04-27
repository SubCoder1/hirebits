from django.contrib import admin
from django.urls import path
from dashboard.views import landing_page_view
from AUth.views import login_view, register_view, reset_view, forgot_pass_view
from dashboard.views import problem_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view.as_view(), name='landing_page'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('fg-pass/', forgot_pass_view, name='forgot_pass'),
    path('rs-pass/', reset_view, name='reset_view'),
    path('problems/', problem_page, name='prob_page'),
]
