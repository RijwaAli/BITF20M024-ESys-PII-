from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'abcdswal'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rijwa@123_ali'
app.config['MYSQL_DB'] = 'system'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['email'] = user['email']
            msg = 'Logged in successfully!'
            flash(msg)
            return redirect(url_for('addStudent'))  # Explicitly redirect to 'addStudent'
        else:
            msg = 'Incorrect email / password!'
            flash(msg)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return render_template('logout.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']

        # Validate the form data
        if not name or not password or not email:
            msg = 'Please fill out all the fields.'
            flash(msg)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
            flash(msg)
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'Username must contain only characters and numbers!'
            flash(msg)
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE name = %s OR email = %s', (name, email,))
            record = cursor.fetchone()

            if record:
                msg = 'User already exists!'
                flash(msg)
            else:
                cursor.execute('INSERT INTO user (name, password, email) VALUES (%s, %s, %s)', (name, password, email,))
                mysql.connection.commit()
                msg = 'You have successfully signed up!'
                flash(msg)

                # Redirect to the add_student route
                return redirect(url_for('add_student'))

    return render_template('signup.html', msg=msg)


@app.route('/addStudent', methods=['GET', 'POST'])
def addStudent():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        full_name = request.form['full_name']
        roll_number = request.form['roll_Number']
        email = request.form['email']
        gender = request.form['gender']
        dob = request.form['dob']
        city = request.form['city']
        interest = request.form['interest']
        department = request.form['department']
        degree_title = request.form['degree']
        subject = request.form['subject']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        cursor = mysql.connection.cursor()
        query = """
            INSERT INTO student (full_name, roll_number, email, gender, dob, city, 
            interest, department, degree_title, subject, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            full_name, roll_number, email, gender, dob, city,
            interest, department, degree_title, subject, start_date, end_date
        )

        cursor.execute(query, values)
        mysql.connection.commit()

        msg = 'Student added successfully!'
        flash(msg)
        return redirect(url_for('addStudent'))

    return render_template('addStudent.html')


def studentList():
    return render_template('studentList.html', students=students)

@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    # Retrieve the student with the given ID (replace this with your actual data retrieval logic)
    student = next((s for s in students if s["id"] == student_id), None)

    if request.method == 'POST':
        # Update the student data (replace this with your actual data update logic)
        student["full_name"] = request.form.get('full_name')
        student["roll_number"] = request.form.get('roll_number')
        student["email"] = request.form.get('email')
        student["gender"] = request.form.get('gender')
        student["dob"] = request.form.get('dob')
        student["city"] = request.form.get('city')
        student["interest"] = request.form.get('interest')
        student["department"] = request.form.get('department')
        student["degree_title"] = request.form.get('degree_title')
        student["subject"] = request.form.get('subject')
        student["start_date"] = request.form.get('start_date')
        student["end_date"] = request.form.get('end_date')

        # Redirect to the StudentList page after updating
        return redirect(url_for('studentList'))

    return render_template('edit.html', student=student)

@app.route('/viewStudent/<int:student_id>')
def viewStudent(student_id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE id = %s', (student_id,))
    student = cursor.fetchone()

    return render_template('viewStudent.html', student=student)


@app.route('/delete/<int:student_id>', methods=['GET'])
def deleteStudent(student_id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM student WHERE id=%s", (student_id,))
    mysql.connection.commit()

    msg = 'Student deleted successfully!'
    flash(msg)
    return redirect(url_for('studentList'))


@app.route('/studentList')
def studentList():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM student')
    students = cursor.fetchall()

    return render_template('studentList.html', students=students)

@app.route('/delete/<int:student_id>')
def delete_confirmation(student_id):

    student = {"id": student_id, "full_name": "John Doe"}  # Replace with actual data
    return render_template('delete.html', student=student)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)
