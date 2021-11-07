import os
import tempfile

import pytest

from app import create_app
from manage import deploy


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        with app.app_context():
            deploy()
        yield client

    os.close(db_fd)
    os.unlink(db_path)