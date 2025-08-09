from django.contrib import admin
from .models import Category,Customer,Product,Order #import the model after migration

# After import model in above, register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

#then after running again, we can see the models are added as table in http://localhost:8000/admin/
# Then add each data
#in product, after save and continue edit 
# (we can see our image direction link with localhost:8000/media/uploads/product/Apple-iPhone-16-Pro-hero-240909_inline.jpg.large_2x.jpg)
#media folder is created after upload and can find the image in there,too and also dbsqlite3 file is also updated


