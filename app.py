from flask import Flask, request, render_template, redirect, url_for
from dto import UserDTO, BoardDTO
from dao import UserDAO, BoardDAO
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html')

@app.route('/membership', methods=['GET', 'POST'])
def membership():   
    return render_template('member.html')

@app.route('/insert', methods=['POST'])
def userinsert():
    global index_user_counter
 
    index_user_counter += 1

    dto = UserDTO(index_user_counter, request.form.get('user_name'), request.form.get('user_pw'), request.form.get('user_interest'))
    dao = UserDAO().userinsert(dto)


    # print("----77-----")

    return  render_template('index.html')

@app.route('/login', methods=['post'])
def userlogin():
    global uname
    uname = request.form.get('user_name')
    # print("-"*30)
    # print(request.form.get('user_name'))
    # print("-"*30)
    
    return UserDAO().userall()

@app.route('/menu', methods=['get'])
def getmenu():
    return render_template('menu.html')

@app.route('/todolist', methods = ['get'])
def gettodolist():
    return render_template('todolist.html')


@app.route('/list', methods = ['get'])
def getlist():
    return render_template('list.html')

@app.route('/char2', methods = ['get'])
def getchar2():
    return render_template('char2.html')

@app.route('/todolist/gettext', methods = ['post'])
def gettext():
    global index_text_counter
    global uname 
    # print(f"로그인 된 이름 : {uname}")
    # print(type(uname))
    index_text_counter += 1
    uid = BoardDAO().getuserID(uname)
    # print(uid)
    # print(uid[0])
    now = datetime.datetime.now()
    # print(now)          
    # 2021-06-22 12:43:19.673801
    nowDate = now.strftime('%Y-%m-%d')
    # print(nowDate)
    # print(type(nowDate))
    dto = BoardDTO(index_text_counter, request.form.get('user_title'), request.form.get('user_text'), nowDate, uid[0])
    print(dto)
    BoardDAO().textinsert(dto)
    return request.form.get('user_title')

@app.route('/list/showlist', methods = ['post'])
def showtext():
    # print("in")
    global uname
    print(uname)
    uid = BoardDAO().getuserID(uname)
    print(uid[0])
    data = BoardDAO().boardall(uid[0])
    # print(data)
    return data

if __name__ == "__main__": 
    index_user_counter = 0 # 초기값 받아오는 걸로 수정하기!
    index_text_counter = 0
    app.run(debug=True, host = "127.0.0.1", port = "5000")