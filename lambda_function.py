import boto3

topic_arn = "arn:aws:sns:us-east-2:827800665158:CTN"
def send_sns(message, subject):
    try:
        client = boto3.client("sns")
        result = client.publish(TopicArn=topic_arn, Message=message, Subject=subject)
        if result['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(result)
            print("Notification send successfully..!!!")
            return True
    except Exception as e:
        print("Error occured while publish notifications and error is : ", e)
        return True

def lambda_handler(event, context):
    print("event collected is {}".format(event))
    for record in event['Records'] :
        sns_topic = record['Sns']['Subject']
        print("Topic name is {}".format(sns_topic))
        sns_data = record['Sns']['Message']
        print("Data is {}".format(sns_data))
        sns_message = "SNS://{}.{}".format(sns_topic, sns_data)
        message = "The SNS is sending a message {}".format(sns_message)
        subject = "Processes completion Notification"
        SNSResult = send_sns(message, subject)
        if SNSResult :
            print("Notification Sent..") 
            return SNSResult
        else:
            return False
