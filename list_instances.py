import boto3
from os.path import exists
from os import getenv

__module__     = 'list_instances.py'
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__updated__    = '20211016.1236'

class InstancesList:
    def __init__(self):
        self._os_check()

    def __call__(self):
        return self.get_all_instances_list()

    def _os_check(self):
        for _file in ['/.aws/config','/.aws/credentials']:
            if not exists(getenv('HOME')+_file):
                raise FileNotFoundError('$HOME'+_file)

    def get_all_instances_list(self):
        instances = []
        ec2 = boto3.resource('ec2')
        for instance in ec2.instances.all():
            instance_name = None
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
            instances.append({'instance_id':instance.id,'instance_name':instance_name})
        return instances


if __name__ == '__main__':
    print(InstancesList()())
