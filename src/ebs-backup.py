import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-west-2')

    # Volume 'Name' Tag
    nametag = ''

    # List only unattached volumes ('available' vs. 'in-use')
    volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}])

    for volume in volumes:
        v = ec2.Volume(volume.id)

        # Get name tag
        nametag = ''
        for tag in v.tags:
            if tag['Key'] == 'Name':
                nametag = tag['Value']

        if not nametag:
            nametag = 'Volume did not have Name tag'

        print('Creating snapshot on: {} for {}'.format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), v.id))
        # snap = v.create_snapshot(Description='Created by ebs-reaper lambda, Tagged: ' +  nametag)


