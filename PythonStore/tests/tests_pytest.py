from app import app

def test_main_page(test_client):
    response = app.get('/')
    assert response.status_code == 200

def test_user_page(test_client):
    response = app.get('/shirts')
    assert response.status_code == 200


def test_admin_page(test_client):
    response = app.get('/shirt/<product_id>')
    assert response.status_code == 200


def test_booking_page(test_client):
    response = app.get('/contact')
    assert response.status_code == 200


def test_showlist_page(test_client):
    response = app.get('/send')
    assert response.status_code == 200

