mkdir video_store && cd video_store
git clone https://github.com/theghost7771/video_store.git
virtualenv -p python3 venv
. venv/bin/activate && cd video_store/
pip install -r requirements/base.txt

./manage.py createsuperuser




Authorization with token:
curl http://localhost:8000/api/v1/api-token-auth/ -d "username=admin;password=password"
{"token":"77535431bf7ed1bfdc38686c571d10b640543eba"}

User creation
curl http://localhost:8000/api/v1/users/ -d "username=user1;password=password" --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"

Or with login/passwrod for testing:
curl http://admin:password@localhost:8000/api/v1/users/ -d "username=user;password=password"
{"username":"user1"}


All videos:
curl http://localhost:8000/api/v1/videos/ --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"

Search by title:
curl http://@localhost:8000/api/v1/videos/?search=title+1 --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"

Get video info:
curl http://localhost:8000/api/v1/videos/1/ --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"

Rent:
curl http://localhost:8000/api/v1/videos/1/rent/ --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"

Return:
curl http://localhost:8000/api/v1/videos/1/rent/ -d "" --header "Authorization: Token 77535431bf7ed1bfdc38686c571d10b640543eba"
