from flask import Flask, request, render_template, redirect, url_for, jsonify, session, flash, g
from flask_jwt_extended import *
from flask_recaptcha import ReCaptcha
from dto import UserDTO, BoardDTO
from dao import UserDAO, BoardDAO
from flask import Blueprint, render_template
from initialize import jwt, recaptcha

bp = Blueprint('pages', __name__, url_prefix='')


@bp.route('/', methods=['POST', 'GET'])
def get():
    message = ''  # Create empty message
    print(request.method)
    if request.method == 'POST':  # Check to see if flask.request.method is POST
        if recaptcha.verify():  # Use verify() method to see if ReCaptcha is filled out
            message = 'Thanks for filling out the form!'  # Send success message
        else:
            message = 'Please fill out the ReCaptcha!'  # Send error message
    return render_template('index.html', message=message)


@bp.route('/membership', methods=['GET', 'POST'])
def membership():
    return render_template('member.html')

@bp.route('/menu', methods=['get'])
def getmenu():
    return render_template('menu.html')


@bp.route('/todolist', methods=['post', 'get'])
def gettodolist():
    return render_template('todolist.html')

@bp.route('/jwttodolist', methods=['post', 'get'])
@jwt_required
def gettodolist():
    return render_template('todolist.html')


@bp.route('/list', methods=['get'])
def getlist():
    return render_template('list.html')


@bp.route('/char2', methods=['get'])
def getchar2():
    return render_template('char2.html')


@bp.route('/index2', methods=['get'])
def getchar3():
    return render_template('index2.html')


@bp.route('/board', methods=['get'])
def getchar4():
    return render_template('board.html')