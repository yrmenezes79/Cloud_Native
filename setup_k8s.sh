apt update 
apt install -y git ansible
git clone https://github.com/yrmenezes79/Cloud_Native
cd Cloud_Native
ansible-playbook setup_k8s.yml
