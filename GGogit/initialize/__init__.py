from flask import Flask, request, render_template, redirect, url_for, jsonify, session, flash, g
from flask_jwt_extended import *
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dto import UserDTO, BoardDTO
from dao import UserDAO, BoardDAO
import datetime
from flask_recaptcha import ReCaptcha
from werkzeug.utils import secure_filename
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import config



recaptcha = ReCaptcha()
jwt = JWTManager()


def create_app(): # 이 이름은 flask 내부적으로 지정됨. 다른걸로 하면 안됨

    #--------------------------Flask 객체 생성---------------------------
    app = Flask(__name__)

    #---------------------------app 설정-----------------------------
    # app.config.from_object(config)
    app.config['RECAPTCHA_SITE_KEY'] = '6LdI60gbAAAAAO9llS8p0UrBetVojtlG-1kuGm-l'
    app.config['RECAPTCHA_SECRET_KEY'] = '6LdI60gbAAAAAPl2g8q9guBs2lFohFUnNNkdpLSQ'
    app.config.update(
        DEBUG=True,
        JWT_SECRET_KEY="DonkeyZZang")
    
    recaptcha.init_app(app)
    jwt.init_app(app)


    #---------------route들을 담는 Blueprint-------------------------------
    # @app 말고 Blueprint를 사용하기 위해 다음과 같이
    # pages.py, functions.py를 불러와서 blueprint를 사용해 실행한다.

    from views import pages  # views 폴더에 pages 모듈을 실행
    from views import functions # views 폴더에 functions 모듈을 실행

    app.register_blueprint(pages.bp) # app에 bp라는 블루프린트를 등록함
    app.register_blueprint(functions.bp)

    return app
    #--------------------------------------------------------------------


if __name__ == "__main__":
    index_user_counter = UserDAO().getIndex()
    index_text_counter = BoardDAO().getTextIndex()
    create_app().run(debug=True, host="127.0.0.1", port="5000")
