from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

def get_common_info():
    os_name = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return os_name, user_agent, current_time

@app.route('/')
def index():
    os_name, user_agent, current_time = get_common_info()
    return render_template('base.html', os_name=os_name, user_agent=user_agent, current_time=current_time)

@app.route('/page1')
def page1():
    os_name, user_agent, current_time = get_common_info()
    return render_template('page1.html', os_name=os_name, user_agent=user_agent, current_time=current_time)

@app.route('/page2')
def page2():
    os_name, user_agent, current_time = get_common_info()
    return render_template('page2.html', os_name=os_name, user_agent=user_agent, current_time=current_time)

@app.route('/page3')
def page3():
    os_name, user_agent, current_time = get_common_info()
    return render_template('page3.html', os_name=os_name, user_agent=user_agent, current_time=current_time)

my_skills = ['Web Development', 'Python Programming', 'Data Analysis', 'Graphic Design']

@app.route('/skills')
@app.route('/skills/<int:id>')
def display_skills(id=None):
    os_name, user_agent, current_time = get_common_info()
    if id is not None:
        if 0 <= id < len(my_skills):
            skill = my_skills[id]
            return render_template('skills.html', skill=skill, os_name=os_name, user_agent=user_agent, current_time=current_time)
        else:
            return "Invalid ID"
    else:
        total_skills = len(my_skills)
        return render_template('skills.html', skills=my_skills, total_skills=total_skills, os_name=os_name, user_agent=user_agent, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
