from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base,User,City,Trip
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



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
	if request.method=='GET':
		return render_template('log_in.html')
	else:
		log_in_email = request.form['email']
		log_in_password = request.form['password']
		check_user=session.query(User).filter_by(email = log_in_email, password = log_in_password).first()
		if check_user == None:
			return render_template('wrong_user.html')
		else:
			return render_template('main_page.html')
	
@app.route('/destination')
def destination():
	cities = session.query(City).all()
	return render_template('choose_destination.html', cities=cities)

@app.route('/destination/<int:city_id>', methods=['GET'])
def select_destination(city_id):
	if request.method=='GET':
		hosts=session.query(User).filter_by(city_id = city_id, experience = 'host').all()
		return render_template('choose_host.html', hosts=hosts)

@app.route('/signup', methods=['GET','POST'])
def sign_up():
	cities=session.query(City).all()
	if request.method=='GET':
		return render_template('sign_up.html', cities=cities)
	else:
		new_city_id = session.query(City).filter_by(name=request.form['city']).first().id
		print(request.form.keys())
		new_name = request.form['name']
		new_pass = request.form['password']
		new_email = request.form['email']
		new_age = request.form['age']
		new_exp = request.form['the_experience']
		new_address = request.form['address']
		new_user = User(name = new_name, age = new_age, email = new_email, password = new_pass, experience = new_exp, city_id=new_city_id, address=new_address)
		session.add(new_user)
		session.commit()
		return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)

