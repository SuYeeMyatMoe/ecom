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

    def add(self,product):
        product_id=str(product.id)

        #logic 
        if product_id in self.cart:#(if they are already added) pass
            pass
        else:
            self.cart[product_id]={'price': str(product.price)}    
        self.session.modified= True

    def __len__(self):#will give filter to get len of things
        return len(self.cart)#will give the quantity of the cart

    def get_items(self):#to see what is in the cart
        #get ids form cart
        product_ids=self.cart.keys()
        #use id to lookup products in database
        products=Products.objects.filter(id_in=product_ids)

        #return those looked up food item prodcuts
        return products
