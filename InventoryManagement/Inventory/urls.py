from django.urls import path
 
from Inventory.views import InventoryDetail
from Inventory.views import InventoryView
from Inventory.views import InventoryList


urlpatterns = [
    path('inventory', InventoryList.as_view()),
    path('api/inventory', InventoryView.as_view()),
    path('inventory/<int:pk>', InventoryDetail.as_view())
]