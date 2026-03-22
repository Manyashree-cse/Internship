from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def  hello():
    return render_template('index.html')

@app.route('/login')
def  login():
    return 'this is login page'

@app.route('/dashboard')
def  dashboard():
    # return 'this is dashoard'
    student_data={
        'student':'manya',
        'course_count':3,
        'grade':95
    }
    return render_template('dashboard.html',**student_data)

@app.route('/courses')
def courses():
    # return "available courses: python,c,java"
    courses=['python','c','java']
    return render_template('courses.html',courses=courses)

@app.route('/home')
def home():
    return render_template('home_extended.html')

@app.route('/submit/<course_name>')
def submit_assignment(course_name):
    message=f'assignment for {course_name} submitted successfully'
    return render_template('success.html',message=message,course=course_name)

if __name__=='__main__':
    app.run(debug=True)