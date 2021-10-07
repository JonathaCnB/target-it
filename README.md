## Download & Instruções para instalação.

* 1 - Clone o projeto: git clone https://github.com/JonathaCnB/target-it.git
* 2 - cd target-it
* 3 - Criar virtual environment: python -m venv venv
* 4 - venv\scripts\activate
* 5 - pip install -r requirements.txt
* 6 - python manage.py migrate
* 7 - python manage.py createsuperuser
* 8 - python manage.py runserver


## Endpoints.

__http_method['post']__
* http://127.0.0.1:8000/api/create-user/
> Endpoint para registro de usuários.
> Requer os dados: first_name, last_name, phone_number, email, password

__http_method['post']__
* http://127.0.0.1:8000/api/login/
> Passando email e senha, assim você obterá seu token de acesso.
> Requer os dados: username (email cadastrado), password

__http_method['get']__
* http://127.0.0.1:8000/api/users/
> Authorization Bearer --------
> Apenas Administradores tem acesso a esse endpoint.

__http_method['get']__
* http://127.0.0.1:8000/api/users/:id/
> Authorization Bearer --------
> Administradores tem acesso a todos os ID's os demais usuários apenas ao seu ID.

__http_method['delete']__
* http://127.0.0.1:8000/api/users/:id/
> Authorization Bearer --------
> Administradores tem acesso a todos os ID's os demais usuários apenas ao seu ID.

__http_method['patch']__
* http://127.0.0.1:8000/api/users/:id/
> Authorization Bearer --------
> Administradores tem acesso a todos os ID's os demais usuários apenas ao seu ID.
