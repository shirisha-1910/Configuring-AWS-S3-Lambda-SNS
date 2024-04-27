import boto3

def lambda_handler(event, context):
    # Extract information from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Customize your notification message
    notification_message = f"New object uploaded: s3://{bucket_name}/{object_key}"
    
    # Send notification (You can use any notification service here like SNS, SES, etc.)
    sns_client = boto3.client('sns')
    sns_client.publish(
        TopicArn='arn:aws:s3:::sns-bucket97543',
        Message=notification_message,
        Subject='New Object Uploaded to S3'
    )
    
    return {
        'statusCode': 200,
        'body': 'Notification sent successfully'
    }
