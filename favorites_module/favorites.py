from product_module.models import ProductModel


class Favorites:
    def __init__(self, request):
        self.session = request.session
        favorites = self.session.get('f_session_key')
        if 'f_session_key' not in request.session:
            favorites = self.session['f_session_key'] = {}

        self.favorites = favorites

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.favorites:
            pass

        else:
            self.favorites[product_id] = str(product_id)

        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.favorites:
            del self.favorites[product_id]

        self.session.modified = True

    def get_prods(self):
        product_ids = self.favorites.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        return products
