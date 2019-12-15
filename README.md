# task-service

## Project setup
install `docker`

### Build the image
```
docker build . -t task-service
```

### Run the development container
```
docker container run -p 5000:5000 task-service
```
then, you will have a server running on 5000 port.

## Endpoints

Do a HTTP request with the given methods to the endpoints below.

### create a new task

```
POST https://yourownhost:5000/v1/tasks/
```

### list all tasks

```
GET https://yourownhost:5000/v1/tasks/ 
```

### list a task with a given id

```
GET https://yourownhost:5000/v1/tasks/<id>
```

### update a task with a given id

```
PUT https://yourownhost:5000/v1/tasks/<id>
```

### delete a task with a given id

```
DELETE https://yourownhost:5000/v1/tasks/<id>
```

