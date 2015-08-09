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




if __name__ == '__main__':
    app.run(debug=True)
