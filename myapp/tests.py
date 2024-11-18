from django.test import TestCase

# Create your tests here.
from .models import Item

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Item 1", description="This is the first item.")
        Item.objects.create(name="Item 2", description="This is the second item.")

    def test_item_str(self):
        item = Item.objects.get(name="Item 1")
        self.assertEqual(str(item), "Item 1")

    def test_item_count(self):
        self.assertEqual(Item.objects.count(), 2)