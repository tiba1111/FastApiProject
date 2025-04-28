from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_client_address():
    def test_get_address():
        # Test the /address endpoint
        response = client.get("/address")
        assert response.status_code == 200

        # You might want to mock the settings in your test
        # for now, assuming the postcode is "75001"
        expected_response = {
            "street": "123 Main Street",
            "city": "Sample City",
            "postcode": "75001"  # Set your expected postcode here
        }

        assert response.json() == expected_response