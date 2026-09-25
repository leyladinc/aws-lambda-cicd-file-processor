import urllib.parse


def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]

    file_name = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    file_size = event["Records"][0]["s3"]["object"]["size"]

    if "." in file_name:
        file_type = file_name.split(".")[-1].lower()
    else:
        file_type = "unknown"

    print(f"New file received: {file_name}")
    print(f"Bucket name: {bucket_name}")
    print(f"File size: {file_size} bytes")
    print(f"File type: {file_type}")
    print("File processing completed successfully")

    return {
        "statusCode": 200,
        "message": "File processed successfully",
        "fileName": file_name,
        "fileType": file_type
    }
