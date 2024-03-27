from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'ls-b640ee9303d25068be488588342687643e09a864.cte0si8k44ty.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'dbmasteruser'
app.config['MYSQL_PASSWORD'] = '3qu1tym3m0rym3m0r1al'
app.config['MYSQL_DB'] = 'Ancestry'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('database_input_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['First_Name']
        last_name = request.form['Last_Name']
        
        # Save data to the database
        cur = mysql.connection.cursor()
        #Auto increment id to prevent duplicate primary keys
        cur.execute("ALTER TABLE enslaved_person MODIFY COLUMN Enslaved_Person_ID INT AUTO_INCREMENT")
        cur.execute("INSERT INTO enslaved_person(First_Name, Last_Name) VALUES (%s, %s)", (first_name, last_name))
        mysql.connection.commit()
        cur.close()
        
        return 'Data inserted successfully.'

if __name__ == '__main__':
    app.run(debug=True)
