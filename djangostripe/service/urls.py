from django.urls import path
from .views import (CreateCheckoutSessionView,
                    CancelView,
                    SuccessView,
                    ProductLandingPageView,
                )

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<int:pk>/', ProductLandingPageView.as_view(), name='item_detail'),
    path('', ProductLandingPageView.as_view(), name='item'),
]
