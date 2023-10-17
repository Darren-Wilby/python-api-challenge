#!/bin/bash

cd "$(dirname "$0")"

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml