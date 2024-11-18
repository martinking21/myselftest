import os
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myselftest.settings')

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Active l'accès à la base de données pour tous les tests automatiquement."""
    pass
