from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
import os
from dotenv import load_dotenv 


app = Flask(__name__)
CORS(app)

load_dotenv() 

admin_username = os.environ.get('ADMIN_USERNAME')
admin_password = os.environ.get('ADMIN_PASSWORD')

@app.route('/')
def home():
    return render_template('login.html') 
@app.route('/login', methods=['POST'])
def login(): 
    data = request.get_json()
    username=data.get('username')
    password=data.get('password')
    if username == admin_username and password == admin_password:
        return jsonify({'success': True, 'message': 'Login successful'}), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    
@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/diary')
def diary():
    return render_template('diary.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)