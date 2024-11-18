from django.test import TestCase
from myapp.models import Item

class TestItemModel(TestCase):
    def test_item_creation(self):
        item = Item.objects.create(name="Sample Item")
        self.assertEqual(item.name, "Sample Item")
