import pytest
from myapp.models import Item

@pytest.mark.django_db
def test_item_creation():
    item = Item.objects.create(name="Sample Item")
    assert item.name == "Sample Item"
