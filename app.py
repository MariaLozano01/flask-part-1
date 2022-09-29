# In order to deploy our app:
#1. Find where app is located on personal laptop
# 2. Change directory in terminal so we can be in the folder that holds code
## 3. 'cd' changes directory
## 4. 'ls' shows what is present in the folder

## 'sudo python3 app.py' --> to deploy our application 
## sudo lsof -t -i:80 --> to check if something is running on a port
## sudo kill -9 $(sudo lsof -t -i:80) --> to quit what is active currently

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/secondtab')
def secondtab():
    return 'This is the second tab of my assignment'

@app.route('/thirdtab')
def thirdtab():
    return 'This is the third tab of my assignment'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

##sudo apt-get update --> to update the terminal we're working in
##Sudo apt install python3-pip --> to install python3 


