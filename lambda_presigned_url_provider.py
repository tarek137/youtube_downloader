
import json
import boto3


def lambda_handler(event, context):

    # Create S3 client and specify region and config
    s3 = boto3.client('s3' , region_name = "eu-west-3" ,
                      config=boto3.session.Config(s3={'addressing_style': 'path'}, signature_version='s3v4'))
    # Create SNS client
    sns = boto3.client('sns')

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # generate the presigned url

    generated_url = s3.generate_presigned_url('get_object',
                                              Params={'Bucket': bucket,
                                                      'Key': key},
                                              ExpiresIn=3600)

    # sending the presigned url
    #Enter the arn of the topic you create to send the email
    response = sns.publish(
        TargetArn= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        Message=json.dumps(generated_url)
    )



    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
