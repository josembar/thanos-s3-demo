#!/bin/bash

AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="989307503852"
IMAGE_NAME="test-app"
OTEL_IMAGE_NAME="otel"
REPO_NAME="test"

docker build -t $IMAGE_NAME ../app

docker build -t $OTEL_IMAGE_NAME ./otel

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

docker tag $IMAGE_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME

docker tag $OTEL_IMAGE_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$OTEL_IMAGE_NAME-latest

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$OTEL_IMAGE_NAME-latest