#!/bin/bash

AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="989307503852"
IMAGE_NAME="test-app"
REPO_NAME="test"

docker build -t $IMAGE_NAME ../app

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

docker tag $IMAGE_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME