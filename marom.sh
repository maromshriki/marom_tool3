#!/bin/bash
set -e

echo "making sure everything is ready"
sudo yum update -y || sudo apt update -y

if command -v yum &> /dev/null; then
    sudo yum install -y python3 
    sudo yum install python3-pip -y
else
    sudo apt install -y python3 
     sudo apt install -y python3-pip 
fi

pip3 install -r requirements.txt


echo "כeverything is ready try:"
echo "python3 cli.py ec2 create --type t2.micro --os ubuntu"
