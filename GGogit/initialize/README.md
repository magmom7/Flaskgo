# blueprint 활용하기
### 아래 영상, 링크들을 참조하여 수정하였습니다.

https://youtu.be/Wfx4YBzg16s
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/11-Blueprints/flaskblog

https://wikidocs.net/81510
https://github.com/pahkey/flaskbook/tree/3-15


### GGogit 수정내역 ( 날짜 )
문제점
    1. jwt, recaptcha 를 쓰기 위해선 각 객체에 app을 등록한 변수를 써야함.  
        그런데 recaptcha = ReCaptcha(app)과 같이 app.py에서 담으면 정작 views폴더의 route들에서 쓸 수가 없다. 
        
        ->
        1) functions.py, pages.py에서 객체로 담은 jwt, recaptcha를 불러올 수 있도록 해야함.  
        2) app.py를 __init__.py로 바꾸고 functions.py, pages.py에서 불러올 수 있도록 하였다.  
        3) __init__.py 로 바꾸면 다른 파일에서 해당 변수를 모듈로 import할 수 있음.
        
        참고  
        https://velog.io/@limes/Python-init.py-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EC%97%AD%ED%95%A0



    
바꾼점
    1. 폴더명을 바꿈.  
        파일명에 .이 들어가있어서.  


추후 수정 사항  
    1. 한 url을 공유하는 route의 경우 따로 blueprint를 만들어서 연결한다.  
        예) /todolist의 경우 todolist라는 url_prefix가 /todolist인 blueprint를 만들어서 '', '/gettext'를 포함 시키기.  
        예2) list도 마찬가지로 showlist, showmylist를 포함시키기.  

    2. @bp.before_app_request를 활용하여 로그인 정보를 지속적으로 확인하기.  

    3. 로그인 과정이 불안정함. 비밀번호가 맞아도 /menu로 넘어가지 않는 문제가 있음.  



### 수정1 
<hr>
6월 23일 17시<br>
로그인 관련 부분 수정<br>
수정 파일 : index.html, app.py, dao.py<br><br>
