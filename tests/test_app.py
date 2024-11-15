import sys
sys.path.append('D:/disha1')  # Add your project directory to the Python path

from app import app  # Now you can import app after modifying the sys.path

import pytest

@pytest.fixture(scope="function")  # Or other scopes: class, module, session
def test_client():
    with app.test_client() as client:
        yield client

@pytest.mark.asyncio  # Mark the test as async since Sanic is asynchronous
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

    # Send the request using the test client
    response = await test_client.post("/process-survey", json=payload)

    # Assert the response status code
    assert response.status_code == 200
    
    # Assert the response JSON body (modify according to your expected response structure)
    expected_response = {
        "status": "success",  # Modify with actual expected response
        "message": "Survey processed successfully",
        # Add other keys that are expected in the response
    }
    
    assert response.json() == expected_response
