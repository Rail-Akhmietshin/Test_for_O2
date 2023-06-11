# Test task for the company O2

## Deployment with Docker

After cloning the repository, grant write permissions for the root and its incoming files and folders:

* chmod -R 755 (your path to the root folder)

Starting the project build:

* docker-compose up -d --build

After successfully running the project in Docker, application will be available at:

* http://localhost:1337

## Web route:

* Route: http://localhost:1337/api/comments/
* Method: GET
* Data: 
```json
{
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
 }, ....
```
