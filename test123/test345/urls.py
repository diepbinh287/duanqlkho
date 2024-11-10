
from django.urls import path
import test345.views

urlpatterns = [
    path('', test345.views.index),
    path('products/', test345.views.product_list, name='product_list'),  # Danh sách sản phẩm
    path('products/<int:product_id>/', test345.views.product_detail, name='product_detail'),  # Chi tiết sản phẩm
    path('stock-in-list/', test345.views.stock_in_list, name='stock_in_list'),  # Danh sách nhập kho
    path('stock-out-list/', test345.views.stock_out_list, name='stock_out_list'),  # Danh sách xuất
    path('add-product/', test345.views.add_product, name='add_product'),  # Thêm sản phẩm
    path('stock-in/', test345.views.stock_in, name='stock_in'),  # Nhập kho
    path('stock-out/', test345.views.stock_out, name='stock_out'),
    path('add-supplier/',  test345.views.add_supplier, name='add_supplier'),
    path('supplier_list/', test345.views.supplier_list, name='supplier_list'),
]