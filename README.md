# NFT_API
## Description
Сервис по производству операции с NFT-токеном, использующий REST API, который получает информацию из блокчейна и выдает ответ в по API в JSON формате, а также изменяет состояние смарт-контракта.

### Tech
Python 3.7, Django 3.2, Rest Framework 3.13, Web3 5.12

### How to start a project:

Clone and move to local repository:

```
git clone https://github.com/Elegantovich/NFT_API/
```
Create a virtual environment (win):
```
python -m venv venv
```
```
cd NFT_TEST
```
Activate a virtual environment:
```
source venv/Scripts/activate
```
Install dependencies from file requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Make migrations:
```
python manage.py makemigrations
```
Run migrations:
```
python manage.py migrate 
```
Run the project:
```
python manage.py runserver
```

| URL| Description |
| ------ | ------ |
| / | start swagger |
| /tokens/create/| POST {'owner': 'input', 'media_url': 'input'} |
| /tokens/list/ | GET |
| /tokens/total_supply/ | GET |

### Checklist:
- [x] Models
- [x] Views + urls + serializers
- [x] Credentials adn keys in .env file
- [x] Mint, total_supply, sign and send_transaction finction
- [x] Pagination for list of tokens
- [x] Working with Web3 library
- [x] Swagger
