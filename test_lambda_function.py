from lambda_function import lambda_handler


def test_lambda_handler():
    test_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-bucket"
                    },
                    "object": {
                        "key": "customer-list.txt",
                        "size": 250
                    }
                }
            }
        ]
    }

    response = lambda_handler(test_event, None)

    assert response["statusCode"] == 200
    assert response["fileName"] == "customer-list.txt"
    assert response["fileType"] == "txt"
