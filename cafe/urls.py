from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ListCreateProduct.as_view(), name='list-create-product'),
    path('product/<str:pk>', views.RetrieveUpdateDestroyProduct.as_view(), name='delete-update-product'),
    path('testimonial/', views.ListCreateTestimonial.as_view(), name='list-create-testimonial'),
    path('testimonial/<str:pk>', views.RetrieveUpdateDestroyTestimonial.as_view, name='delete-update-testimonial'),
    path('cafeinfo/', views.RetrieveUpdateCafeInfo.as_view(), name='get-update-cafeInfo'),
    path('gallery/', views.ListCreateGallery.as_view(), name='list-create-gallery'),
    path('gallery/<str:pk>', views.RetrieveDestroyGallery.as_view(), name='delete-update-gallery'),
    path('recaptcha/', views.recaptcha, name="recaptcha")
]