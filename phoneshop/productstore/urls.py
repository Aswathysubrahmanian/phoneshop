from django.urls import path
from productstore import views
urlpatterns = [
    #path('phones/add/',views.addPhone.as_view(),name='addphone'),
path('phones/add/',views.add_phone,name='addphone'),
    #path('phones/display/',views.display_phone.as_view(),name="display_phone"),
path('phones/display/',views.display,name='display_phone'),
    #path('phones/details/<int:id>/',views.View.as_view(),name='phone_details'),
    path('phones/details/<int:id>/', views.view, name='phone_details'),

    path('',views.ownerpage,name="ownerpage"),
    path('phones/listof/<int:id>/',views.change_phone,name="edit_phone"),
    path('phones/del/<int:id>/',views.remove_phone,name="delete_phone"),
    path('accounts/register/',views.UserRegistrationForm,name='register'),
    path('accounts/signin/',views.Signin,name='login'),
    path('accounts/logout/',views.SignOut,name='logout')


]
