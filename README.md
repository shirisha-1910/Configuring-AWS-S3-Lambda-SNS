# Configuring-AWS-S3-Lambda-SNS

# AWS S3 Upload Notification System

This project sets up an AWS S3 upload notification system using AWS Lambda, SNS, and S3. When an object is uploaded to an S3 bucket, a Lambda function is triggered, which publishes a notification to an SNS topic. Subscribers to the SNS topic receive notifications, enabling real-time awareness of S3 bucket activity.

## Setup Instructions

1. **Create AWS Resources**:
   - Create an S3 bucket to monitor for object uploads.
   - Set up an SNS topic to receive notifications.
   - Create a Lambda function to trigger on S3 upload events and publish to the SNS topic.

2. **Lambda Function Configuration**:
   - Write the Lambda function code to handle S3 upload events and publish notifications to the SNS topic.
   - Configure the Lambda function with appropriate permissions to access S3 and SNS.

3. **Subscribe to SNS Topic**:
   - Subscribe to the SNS topic using your desired endpoint (e.g., email) to receive notifications.

4. **Testing**:
   - Upload an object to the S3 bucket to trigger the Lambda function.
   - Verify that notifications are successfully delivered via the subscribed endpoint.

## Triggering Lambda Function Using Python Script

To programmatically trigger the Lambda function, you can use the provided Python script [`notify.py`](notify.py). This script utilizes the AWS SDK for Python (Boto3) to invoke the Lambda function.

### Installation

1. Install the Boto3 library:
   ```bash
   pip install boto3
