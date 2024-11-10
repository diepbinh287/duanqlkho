from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import ProductForm,StockInForm,StockOutForm,SupplierForm

def index(request):
    return render(request, 'base.html')

# Function-based view to display all products
def product_list(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm
    return render(request, 'product_list.html', {'products': products})
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # Lấy sản phẩm theo ID
    return render(request, 'product_detail.html', {'product': product})
def stock_in_list(request):
    stock_in_items = StockIn.objects.all()  # Lấy tất cả các giao dịch nhập kho
    return render(request, 'stock_in_list.html', {'stock_in_items': stock_in_items})
def stock_out_list(request):
    stock_out_items = StockOut.objects.all()  # Lấy tất cả các giao dịch xuất kho
    return render(request, 'stock_out_list.html', {'stock_out_items': stock_out_items})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu sản phẩm vào cơ sở dữ liệu
            return redirect('product_list')  # Quay lại danh sách sản phẩm
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def stock_in(request):
    if request.method == 'POST':
        form = StockInForm(request.POST)
        if form.is_valid():
            stock_in_item = form.save()  # Lưu thông tin nhập kho
            # Cập nhật số lượng trong kho của sản phẩm
            product = stock_in_item.product
            product.quantity_in_stock += stock_in_item.quantity
            product.save()
            return redirect('stock_in_list')  # Quay lại danh sách nhập kho
    else:
        form = StockInForm()

    return render(request, 'stock_in.html', {'form': form})

def stock_out(request):
    if request.method == 'POST':
        form = StockOutForm(request.POST)
        if form.is_valid():
            stock_out_item = form.save()  # Lưu thông tin xuất kho
            # Cập nhật số lượng trong kho của sản phẩm
            product = stock_out_item.product
            if product.quantity_in_stock >= stock_out_item.quantity:
                product.quantity_in_stock -= stock_out_item.quantity
                product.save()
                return redirect('stock_out_list')  # Quay lại danh sách xuất kho
            else:
                form.add_error('quantity', 'Số lượng xuất kho vượt quá số lượng tồn kho!')
    else:
        form = StockOutForm()

    return render(request, 'stock_out.html', {'form': form})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu nhà cung cấp vào cơ sở dữ liệu
            return redirect('supplier_list')  # Quay lại danh sách nhà cung cấp
    else:
        form = SupplierForm()

    return render(request, 'add_supplier.html', {'form': form})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})




