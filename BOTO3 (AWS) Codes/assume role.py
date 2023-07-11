import boto3


sts = boto3.client('sts', region_name='your_region', aws_access_key_id='your_access_key', aws_secret_access_key='your_secret_key')


response = sts.assume_role(
    RoleArn='arn:aws:iam::your_account_id:role/your_role_name',
    RoleSessionName='your_session_name'
)


credentials = response['Credentials']

# Set up the EC2 client with the temporary credentials
ec2 = boto3.client(
    'ec2',
    region_name='your_region',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)

# Create the EC2 instance using the assumed role
# ...

# Rest of your code
