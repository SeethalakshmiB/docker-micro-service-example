# Docker flask app + RDS

* build image
```
    docker build --build-arg DB_USERNAME="admin" \
    --build-arg DB_PASSWORD="admin-123" \
    --build-arg DB_NAME="abc" \
    --build-arg DB_HOST="test1.abc.us-east-1.rds.amazonaws.com" \
    -t abc .
```

setup docker in ec2 instance
```
yum update -y
yum install docker -y
systemctl 


* run a container in a server
```
docker run   -p 8081:5000 abc

```