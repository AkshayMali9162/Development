import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2', region_name='your_region', aws_access_key_id='your_access_key', aws_secret_access_key='your_secret_key')

# Create the EC2 instance
response = ec2.run_instances(
    ImageId='your_ami_id',
    InstanceType='your_instance_type',
    KeyName='your_key_pair_name',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=['your_security_group_id'],
    SubnetId='your_subnet_id'
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']

print(f"Instance ID: {instance_id}")
