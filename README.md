# 2024-Herethon-6
2024 여기톤 : HERETHON 6조


<h1>👨‍💻 Role & Contribution</h1>
<hr>
<h2>기획/디자인</h2>

<li>전수민(서울여자대학교)</li>

<h2>프론트엔드</h2>

<li>김예원(이화여자대학교)</li>
<li>김정은(성신여자대학교)</li>

<h2>백엔드</h2>

<li>손재윤(덕성여자대학교)</li>
<li>김민주(동덕여자대학교)</li>

<hr>
<h1>Title</h1>

<hr>
<li>폴더구조</li>

```
mzSkill/
├── accounts/
├── chat/
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   └── chat/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── community/
├── main/
├── matching/
├── media/
├── mzSkill/
├── profiles/
├── review/
├── static/
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── .gitignore
```


<li>개발환경 실행방법</li>

```
$ python -m venv myvenv    #가상환경 생성
$ source newvenv/Scripts/activate
$ pip install pillow
$ pip install django
$ cd mzSkill
$ docker-compose up
```

