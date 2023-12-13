from flask import Flask, request, jsonify
import pymysql
import uuid
import boto3
from botocore.exceptions import ClientError

# MySQL database configuration
MYSQL_CONFIG = {
    'host': 'your-database-host',  # Replace with your database host address
    'user': 'your-database-user',  # Replace with your database username
    'password': 'your-database-password',  # Replace with your database password
    'db': 'your-database-name',  # Replace with your database name
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

app = Flask(__name__)

@app.route('/notify', methods=['GET'])
def notify():
    # Example response for GET request
    return jsonify({'message': 'GET request received'}), 200

# Other helper functions (send_forum_message_notification, create_post, etc.) remain unchanged

def send_notification(recipient, subject, message):
    # Use AWS SNS to send notifications (same as in your Lambda function)
    sns_client = boto3.client('sns')
    try:
        sns_client.publish(
            TopicArn='arn:aws:sns:region:account-id:topic-name',  # Replace with your SNS topic ARN
            Message=message,
            Subject=subject
        )
        print("Notification sent successfully to SNS topic!")
    except ClientError as e:
        print(f"An error occurred: {e}")
        raise

def generate_unique_post_id():
    return str(uuid.uuid4())

def generate_unique_comment_id():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
