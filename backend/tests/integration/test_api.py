from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)


class TestCalculateEndpoint:
    """Integration tests for the /api/calculate endpoint."""

    def test_calculate_success(self):
        """Tests a successful calculation (n=10)."""
        # Arrange
        payload = {"number": 10}

        # Act
        response = client.post("/api/calculate", json=payload)
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert "result" in data
        assert "sequence" in data
        assert data["result"] == 55
        assert data["sequence"] == [5, 8, 13, 21, 34]

    def test_calculate_invalid_input_negative(self):
        """Tests the endpoint with an invalid negative number."""
        # Arrange
        payload = {"number": -5}

        # Act
        response = client.post("/api/calculate", json=payload)

        # Assert
        assert response.status_code == 422  # Unprocessable Entity

    def test_calculate_invalid_input_too_large(self):
        """Tests the endpoint with a number greater than 100."""
        # Arrange
        payload = {"number": 101}

        # Act
        response = client.post("/api/calculate", json=payload)

        # Assert
        assert response.status_code == 422

    def test_calculate_invalid_input_non_integer(self):
        """Tests the endpoint with a non-integer value."""
        # Arrange
        payload = {"number": "abc"}

        # Act
        response = client.post("/api/calculate", json=payload)

        # Assert
        assert response.status_code == 422


if __name__ == "__main__":
    pytest.main()
