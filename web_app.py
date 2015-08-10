from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base,User,City,Trip
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#engine = create_engine('sqlite:///crudlab.db')
#Base.metadata.bind = engine
#DBSession = sessionmaker(bind=engine)
#session = DBSession()



@app.route('/')
def main():
    return render_template('main_page.html')

##@app.route('/')
##def main():
	##user = session.query(User).first()
	##return render_template("main_page.html",user=user)

@app.route('/aboutus')
def about_us():
    return render_template('about_us.html')

@app.route('/login')
def log_in():
    return render_template('log_in.html')

@app.route('/signup')
def sign_up():
    return render_template('sign_up.html')



if __name__ == '__main__':
    app.run(debug=True)
