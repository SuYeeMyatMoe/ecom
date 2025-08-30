from store.models import Product #access Product model to get product ids
class Cart():
    def __init__(self,request):
        self.session= request.session

        #get the current session key if exists 
        cart= self.session.get('session_key')

        #if the user is new, no session key! create new one!
        if 'session_key' not in request.session:
            cart= self.session['session_key']={}

        #make sure cart is working on every pages and files
        self.cart=cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id] += product_qty   #  increment
        else:
            self.cart[product_id] = product_qty    # first time add

        self.session.modified = True


    def __len__(self):#will give filter to get len of things
        return sum(self.cart.values())#will give the quantity of the cart

    def get_items(self):#to see what is in the cart
        #get ids form cart
        product_ids=self.cart.keys()
        #use id to lookup products in database
        products=Product.objects.filter(id__in=product_ids)

        #return those looked up food item products
        return products
    
    def get_quants(self):
        quantities=self.cart
        return quantities
    
    def delete(self, product):
        product_id=str(product)#change dictionary into string 

        #delete from dictionary cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True

    def cart_total(self):  
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:  
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value 
        return total




    