from django.urls import path
from .views import APIToken, APITotalSupply, APITokenList


urlpatterns = [
    path('create/', APIToken.as_view()),
    path('list/', APITokenList.as_view()),
    path('total_supply/', APITotalSupply.as_view())
]
