import os
import pytest
from app import app

# Setting up a temporary test environment
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = 'test_uploads'  # Prevent actual uploads
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    with app.test_client() as client:
        yield client
    # Cleanup after test
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
    os.rmdir(app.config['UPLOAD_FOLDER'])

def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    # assert b"Upload File" in response.data

def test_algo_closest_pair(client):
    """Test the algorithm closest_pair route with file upload"""
    data = {
        'input_file': (open('test_cp.txt', 'rb'), 'test_cp.txt')
    }
    response = client.post('/algo/closest_pair', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Closest pair" in response.data

def test_algo_int_multiplication(client):
    """Test the algorithm int_multiplication route with file upload"""
    data = {
        'input_file': (open('test_im.txt', 'rb'), 'test_im.txt')
    }
    response = client.post('/algo/int_multiplication', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Karatsuba result" in response.data
