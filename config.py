# http://cloud-images.ubuntu.com/locator/ec2/
REGION = 'ap-southeast-1'
AMI = 'ami-a02f66f2'
SIZE = 't1.micro'


HTTP_ACCESS_IP = '0.0.0.0'

# You will have to fork my repository, configure SSH keys for deploy and
# then set the paths here. More information can be found here:
#
#         https://help.github.com/articles/managing-deploy-keys
#
DEPLOY_PRIVATE_PATH = 'keys/github_id_rsa'
DEPLOY_PUBLIC_PATH = 'keys/github_id_rsa.pub'
