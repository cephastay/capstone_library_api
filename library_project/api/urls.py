from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import BookViewSet, AvailableBooks

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'available', AvailableBooks, basename='available')
# router.register(r'books/<int:pk>/detail/', BookViewSet, basename='book-retrieve')
# router.register(r'books/<int:pk>/update/', BookViewSet, basename='book-update')
# router.register(r'books/<int:pk>/delete/', BookViewSet, basename='book-destroy')
# router.register(r'books/', BookViewSet, basename='book-list')
# router.register(r'books/<int:pk>/checkout', BookViewSet, basename='checkout_book')

urlpatterns = [
    path('', include(router.urls))
]