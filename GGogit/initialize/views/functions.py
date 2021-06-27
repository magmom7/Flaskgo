from flask import Flask, request, render_template, redirect, url_for, jsonify, session, flash, g
from flask_jwt_extended import *
from dto import UserDTO, BoardDTO
from dao import UserDAO, BoardDAO
from flask import Blueprint, render_template
from werkzeug.utils import secure_filename
import datetime
from initialize import jwt, recaptcha
# 이거 읽은거임

bp = Blueprint('functions', __name__, url_prefix='/')

@bp.route('/insert', methods=['POST'])
def userinsert():
    global index_user_counter
    index_user_counter = 0
    index_user_counter += 1

    dto = UserDTO(index_user_counter, request.form.get('user_name'),
                  request.form.get('user_pw'), request.form.get('user_interest'))
    
    if UserDAO().userone(request.form.get('user_name'), request.form.get('user_pw')) == True:
        return jsonify(result='idexist', messege='this id already exists')
    else:
        dao = UserDAO().userinsert(dto)
        return jsonify(result='signup', messege='signup success')



@bp.route('/login', methods=['post'])
def userlogin():
    uname = request.form.get('username')
    upw = request.form.get('userpw')

    data = UserDAO().userone(uname, upw)
    print(data)
    if data is False:
        return jsonify(result='login_fail')
    else:
        # session['user_id'] = uname
        return jsonify(result = 200, access_token=create_access_token(identity=uname))



@bp.route("/jwtconfirm")
@jwt_required()   # 참조 사이트에선 () 표현이 누락, 즉 버전에 따른 차이
def jwt_confirm():
    cur_user = get_jwt_identity()
    # if cur_user = 
    print("회원 이름 : "+ cur_user + " 접속")
    return jsonify(id=cur_user, result = 200)



@bp.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    return render_template('menu.html')


@bp.route('/todolist/gettext', methods=['post'])
@jwt_required()
def gettext():
    global index_text_counter
    cur_user = get_jwt_identity()
    index_text_counter = 0
    index_text_counter += 1
    
    dao = BoardDAO()
    uid = dao.getuserID(cur_user)
    now = datetime.datetime.now()
 
    nowDate = now.strftime('%Y-%m-%d')

    dto = BoardDTO(index_text_counter, request.form.get(
        'user_title'), request.form.get('user_text'), nowDate, uid[0])

    BoardDAO().textinsert(dto)
    return request.form.get('user_title')


@bp.route('/list/showlist', methods=['post'])
def showtext():
    data = BoardDAO().boardall()

    return data

@bp.route('/list/showmylist', methods=['post'])
@jwt_required()
def showmytext():
    cur_user = get_jwt_identity()

    uid = BoardDAO().getuserID(cur_user)
    data = BoardDAO().boardmy(uid[0])
    
    return data