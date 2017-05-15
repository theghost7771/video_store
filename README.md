# Project start #
```
mkdir video_store && cd video_store
git clone https://github.com/theghost7771/video_store.git
virtualenv -p python3 venv
. venv/bin/activate && cd video_store/
pip install -r requirements/base.txt

./manage.py createsuperuser
./manage.py runserver
```



## Authorization with token ##
```
curl http://localhost:8000/api/v1/api-token-auth/ -d "username=admin;password=password"
{"token":"77535431bf7ed1bfdc38686c571d10b640543eba"}
```
## User creation ##
```
curl http://localhost:8000/api/v1/users/ -d "username=user1;password=password" --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
{"username":"user1"}
```
## Or with login/passwrod for testing ## 
```
curl http://admin:password@localhost:8000/api/v1/users/ -d "username=user;password=password"
{"username":"user"}
```

## All videos ## 
```
curl http://localhost:8000/api/v1/videos/ --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
{
"next":null,
"previous":null,
"results":[
    {
        "title":"Title 10",
        "is_available":true,
        "url":"http://localhost:8000/api/v1/videos/10/",
        "id":10},
        {"title":"Title 9"
        ...
```
## Search by title ##
```
curl http://@localhost:8000/api/v1/videos/?search=title+1 --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
{
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 10,
            "is_available": true,
            "title": "Title 10",
            "url": "http://localhost:8000/api/v1/videos/10/"
        },
        {
            "id": 1,
            "is_available": false,
            "title": "Title 1",
            "url": "http://localhost:8000/api/v1/videos/1/"
        }
    ]
}

```
## Get video info ##
```
curl http://localhost:8000/api/v1/videos/1/ --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
{
    "id": 1,
    "is_available": false,
    "title": "Title 1",
    "url": "http://localhost:8000/api/v1/videos/1/"
}

```
## Rent ##
```
curl http://localhost:8000/api/v1/videos/1/rent/ -d "" --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
{"success":true}
```
## Return ##
```
curl http://localhost:8000/api/v1/videos/1/rent/ -d "" --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
{"success":true}
```
