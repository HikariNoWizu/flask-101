# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_get_product(self):
        response = self.client.get("/api/v1/products/1")
        self.assertEquals(response.status_code, 200)
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertGreater(len(product), 1)
        self.assertEquals(product, dict({'id': 1, 'name': 'Skello'}))

    def test_get_product_return_404(self):
        response = self.client.get("/api/v1/products/7")
        self.assertEquals(response.status_code, 404)

    #def test_delete_one_product(self):
    #    response = self.client.delete("/api/v1/products/2")
    #    self.assertEquals(response.status_code, 204)
    # il faut le réinsérer derriere

    def test_add_one_product(self):
        response = self.client.post("/api/v1/product", json={'name': 'Netflix'})
        self.assertEquals(response.status_code, 201)

    def test_update_one_product(self):
        response = self.client.patch("/api/v1/product/3", json={'name': 'Netflix'})
        self.assertEquals(response.status_code, 204)

    def test_update_one_product_raises_422(self):
        response = self.client.patch("/api/v1/product/7", json={'name': 'Netflix'})
        self.assertEquals(response.status_code, 422)
