import boto3

DYNAMODB = boto3.resource('dynamodb', endpoint_url='https://dynamodb.eu-central-1.amazonaws.com')
job_history_table = DYNAMODB.Table('job_history')

if __name__ == '__main__':
    print('Testing...')
    print(job_history_table.scan())