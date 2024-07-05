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
<h2>독창성 있는 티칭에 자신있거나 새로운 배움에 도전하고 싶은 MZ세대가 만드는 1:1 맞춤 티쳐 매칭 웹 서비스, MZ의 스킬</h2>

가르침을 전수하기 원하신다면, 나만의 티칭 능력을 발휘하고 싶은 MZ세대라면 이 서비스를 통해 멘토가 될 수 있습니다!
당신은 다양한 러너분들을 모시면서 창의적인 아이디어와 감각으로 나만의 티칭 능력과 경험을 쌓을 수 있어 의미있는 서비스가 될 것입니다.

가르침 받기를 원하시나요? 기발한 아이디어로 구상된 티칭을 배우고 싶은 MZ세대라면 러너를 추천드립니다. 러너분들이 원하는 티쳐의 타입과 관심있는 스킬 분야를 참고하여 1:1 맞춤 MZ 티쳐를 소개해드릴수 있습니다.

러너분들은 다양한 카테고리의 스킬 분야에서 MZ의 티칭을 접할 수 있고, 
디지털 소통으로 이루어지는 티칭이므로 불필요한 관계 형성을 강요하지않기에 친목과 배움을 아우르는 완벽한 커뮤니티를 형성할 수 있습니다.

나만의 MZ 티쳐를 만나보고 싶다면 MZ의 스킬을 활용해보세요.

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
$ source myvenv/Scripts/activate
$ pip install pillow
$ pip install django
$ cd mzSkill
$ docker-compose up
```
*Django에서 Channels라이브러리를 이용한 비동기 통신 과정을 진행했습니다.
요청-응답의 단방향통신과 구분되는 서버와 클라이언트간 메세지의 양방향 교환을 구현했으며 이를 통해 브라우저에서 WebSocket 서버로 요청이 들어오면 HTTP에서는 미리 구축해놓은 라우팅파일을 이용해 HTTP -> WS로 프로토콜을 전환 후 메세지 단위로 전달할 수 있습니다.*
