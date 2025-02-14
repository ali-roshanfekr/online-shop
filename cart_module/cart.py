from product_module.models import ProductModel


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        if product_id in self.cart:
            pass

        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        cart = self.cart
        cart[product_id] = product_qty
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def total(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        total = 0
        for product in products:
            total += product.price * self.cart[str(product.id)]

        return total
