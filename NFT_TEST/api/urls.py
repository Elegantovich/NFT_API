from django.urls import path, include

urlpatterns = [
    path('create/', SendMessageForToken.as_view()),
    path('list/', SendMessageForConfirmationCode.as_view()),
    path('total_supply/', include(v1_router.urls))
]