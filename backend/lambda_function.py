import json
import openai
import os
import boto3
import uuid

# Load environment variables
openai.api_key = os.environ["OPENAI_API_KEY"]
bucket_name = os.environ["S3_BUCKET_NAME"]

s3 = boto3.client('s3')

def upload_to_s3(file_data, file_name):
    unique_file_name = f"{uuid.uuid4()}-{file_name}"
    s3.put_object(Bucket=bucket_name, Key=unique_file_name, Body=file_data)
    return f"https://{bucket_name}.s3.amazonaws.com/{unique_file_name}"

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_input = body['user_input']
        file_data = body.get('file_data')
        file_name = body.get('file_name')

        uploaded_file_url = None
        if file_data and file_name:
            decoded_file_data = bytes(file_data, 'utf-8')
            uploaded_file_url = upload_to_s3(decoded_file_data, file_name)

        # Generate OpenAI response
        prompt = f"""You are a sales enablement expert. Based on the following requirements, generate a sales strategy recommendation:

User Input: {user_input}
File Reference: {uploaded_file_url if uploaded_file_url else "No file uploaded"}
"""

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        assistant_response = response['choices'][0]['text'].strip()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "assistant_response": assistant_response,
                "file_url": uploaded_file_url
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
