import pytest
from app import app

@pytest.fixture
def test_client():
    return app.test_client

async def test_process_survey_success(test_client):
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
    response = await test_client.post("/process-survey", json=payload)
    assert response.status == 200
