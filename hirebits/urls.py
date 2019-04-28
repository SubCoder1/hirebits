from django.contrib import admin
from django.urls import path
from dashboard.views import landing_page_view
from AUth.views import login_view, register_view, reset_view, forgot_pass_view, logout_view
from dashboard.views import problem_page
from dashboard.views import dashboard_page
from dashboard.views import learn_page
from dashboard.views import solve_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view.as_view(), name='landing_page'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_view, name='register_view'),
    path('fg-pass/', forgot_pass_view, name='forgot_pass'),
    path('rs-pass/', reset_view, name='reset_view'),
    path('problems/', problem_page, name='prob_page'),
    path('dashboard/', dashboard_page, name='dash_page'),
    path('learn/', learn_page, name='lea_page'),
    path('solve/', solve_page, name='solve_page'),
]
