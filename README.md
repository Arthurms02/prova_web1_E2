# 📚 Home Task

## Descrição
Este projeto foi desenvolvido para a avaliação da disciplina de Web1 do curso de ADS da UNIFIP. Utilizamos Django como tecnologia principal e HTML, CSS e Bootstrap para criar um banco de questões, permitindo que os usuários respondam perguntas para se prepararem para vestibulares e provas. Além disso, a plataforma oferece a possibilidade de um usuário se tornar professor e criar suas próprias questões.


# 🚀 Instruções de Execução

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
 ```
## 🧩 Modifique o banco de dados no settings
```python
DATABASE ={
	'default':  {
		'ENGINE':  'django.db.backends.sqlite3',
		'NAME':  BASE_DIR  /  'db.sqlite3',
	}
}

```
------

```bash
python manage.py loaddata app/fixtures/questoes.json
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
 ```