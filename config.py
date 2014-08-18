# http://cloud-images.ubuntu.com/locator/ec2/
REGION = 'us-east-1'
AMI = 'ami-b2b061da'
SIZE = 't2.micro'


DEFAULT_SEC_GROUP = 'default'


HTTP_ACCESS_IP = '0.0.0.0/0'

# You will have to fork my repository, configure SSH keys for deploy and
# then set the paths here. More information can be found here:
#
#         https://help.github.com/articles/managing-deploy-keys
#
DEPLOY_PRIVATE_PATH = 'keys/id_rsa'
DEPLOY_PUBLIC_PATH = 'keys/id_rsa.pub'
