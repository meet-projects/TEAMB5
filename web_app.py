from flask import Flask, render_template, request, url_for, redirect
from flask import session as web_session
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

@app.route('/login' ,methods=['GET','POST'])
def log_in():
	if request.method=='GET':
		return render_template('log_in.html')
	else:
		log_in_email = request.form['email']
		log_in_password = request.form['password']
		check_user=session.query(User).filter_by(email = log_in_email, password = log_in_password).first()
		if check_user == None:
			return redirect(url_for('wrong_user'))
		else:
			web_session['my_user_id'] = check_user.id
			return redirect(url_for('main'))
	
@app.route('/destination')
def destination():
	cities = session.query(City).all()
	return render_template('choose_destination.html', cities=cities)

@app.route('/wrong_user')
def wrong_user():
	return render_template('wrong_user.html')

@app.route('/destination/<int:city_id>', methods=['GET','POST	'])
def select_host(city_id):
	if request.method=='GET':
		hosts=session.query(User).filter_by(city_id = city_id, host = True).all()
		print(hosts)
		return render_template('choose_host.html',city_id = city_id, hosts=hosts)
	else:
		visitor_id = web_session['my_user_id']
		host_id = request.form['host_id']
		destination_id = city_id
		new_trip = Trip(host_id = host_id, visitor_id = visitor_id, destination_id = destination_id)
		session.add(new_trip)
		session.commit()
		return redirect(url_for('profile'))

	
@app.route('/profile')
def profile():
	if 'my_user_id' in web_session:
		my_user = session.query(User).filter_by(id = web_session['my_user_id']).first()
		if my_user.host:
			my_hosted_trips = session.query(Trip).filter_by(host_id = my_user.id).all()
		else: 
			my_hosted_trips = None
		if my_user.visit or my_user.study:
			my_trips = session.query(Trip).filter_by(visitor_id = my_user.id).all()
		else: 
			my_trips = None
		print(my_trips)
		print(my_hosted_trips)
		return render_template('profile.html',my_user = my_user, my_hosted_trips=my_hosted_trips , my_trips=my_trips)
	return redirect(url_for('wrong_user'))
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
		new_purposes = request.form.getlist('purposes')
		new_study = 'study' in new_purposes
		new_host = 'host' in new_purposes
		new_visit = 'visit' in new_purposes
		new_address = request.form['address']
		new_user = User(name = new_name, age = new_age, email = new_email, password = new_pass, 
			host = new_host, study = new_study, visit = new_visit, city_id=new_city_id, address=new_address)
		session.add(new_user)
		session.commit()
		return redirect(url_for('log_in'))


if __name__ == '__main__':
	app.secret_key = "s8KxYJ3SFsFNqF2PdY3ybd5Q"
	app.run(debug=True)

