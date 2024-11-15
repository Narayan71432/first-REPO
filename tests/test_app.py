import pytest
from app import app

@pytest.fixture
def test_client():
    # Return the test client correctly
    with app.test_client() as client:
        yield client

def test_process_survey_success(test_client):
    payload = {
        "user_id": "test_user",
        "survey_results": [
            {"question_number": 1, "question_value": 5},
            {"question_number": 2, "question_value": 6},
            {"question_number": 3, "question_value": 4},
            {"question_number": 4, "question_value": 3},
            {"question_number": 5, "question_value": 7},
            {"question_number": 6, "question_value": 5},
            {"question_number": 7, "question_value": 6},
            {"question_number": 8, "question_value": 7},
            {"question_number": 9, "question_value": 5},
            {"question_number": 10, "question_value": 6}
        ]
    }

    # Send the request using the test client
    response = test_client.post("/process-survey", json=payload)

    # Assert the response status code
    assert response.status_code == 200
