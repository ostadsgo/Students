import datetime as dt
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from itsdangerous import URLSafeSerializer
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = '1e88361a5400e55d138d23fc71547ff4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'saeed.ghollami@gmail.com',
    MAIL_PASSWORD = 'k@rs!zP4ssw0rd'
))
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
serializer = URLSafeSerializer(app.config['SECRET_KEY'])


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# User Table
class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    personal_details = db.Column(db.String(256))
    description = db.Column(db.String(256))
    confirmed = db.Column(db.Boolean(), default=False)
    events = db.relationship('Event', backref='user')
    attendees = db.relationship('Attendee', backref='user')

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return self.username


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    date = db.Column(db.Date, nullable=False, default=dt.datetime.now().date())
    description = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_category = db.Column(db.Integer, db.ForeignKey('event_category.cat_id'), nullable=False)


class EventCategory(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)



class Attendee(db.Model):
    att_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)

    def __repr__(self):
        user = User.query.filter_by(user_id=self.user_id).first()
        return user.username


# class Message:
#     message_id = db.Column(db.Integer, primary_key=True)
#     recipient = db.Column(db.String(), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')  # 
        email = request.form.get('email')
        # generate token and message to send to user
        token = serializer.dumps(email)
        confirm_link = url_for('confirm_email', token=token, _external=True)
        msg = Message('Confirm Email', sender='saeed.ghollami@gmail.com', recipients=[email], html=render_template('confirm.html', confirm_url=confirm_link))
        # msg.body = f'Your confirmation link is {confirm_link}'
        mail.send(msg)
        # password hashing
        hashed_pw = bcrypt.generate_password_hash(request.form.get('password'))
        user = User(username=username, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('You were successfully registerd.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')



@app.route('/confirm_email/<token>')
def confirm_email(token):
    email = serializer.loads(token)
    user = User.query.filter_by(email=email).first()
    user.confirmed = True
    db.session.commit()

    login_user(user)
    return redirect('dashboard')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and bcrypt.check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful.', 'danger')
    
    events = Event.query.all()
    return render_template('index.html', events=events)


@app.route('/addevent', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':
        name = request.form.get('name')
        date = dt.datetime.strptime(request.form.get('date'), '%Y-%m-%d')
        cat = request.form.get('cat')
        desc = request.form.get('desc')
        event = Event(name=name, date=date, event_category=cat, 
                      description=desc, user_id=current_user.user_id)
        db.session.add(event)
        db.session.commit()
        flash('Event were successfully added.', 'success')
    return render_template('add_event.html')


@app.route('/myevents')
@login_required
def my_events():
    attendees = {}
    events = Event.query.filter_by(user_id=current_user.user_id).all()
    
    # Find attendees to current user's events
    for event in events:
        joiners = Attendee.query.filter_by(event_id=event.event_id).all()
        attendees[event.event_id] = joiners
    
    print(attendees)
    return render_template('my_events.html', events=events, attendees=attendees)


@app.route('/delevent/<int:event_id>')
@login_required
def delete_event(event_id):
    event = Event.query.filter_by(event_id=event_id).first()
    attendees = Attendee.query.filter_by(event_id=event_id).all()
    print(attendees)
    db.session.delete(event)
    for attendee in attendees:
        db.session.delete(attendee)
    db.session.commit()
    flash('event deleted', 'info')
    return redirect(url_for('my_events'))


@app.route('/join_event/<int:user_id>/<int:event_id>')
@login_required
def join_event(user_id, event_id):
    a_join = Attendee(user_id=user_id, event_id=event_id)
    event = Event.query.filter_by(event_id=event_id).first()
    db.session.add(a_join)
    db.session.commit()
    flash(f'You joined Successfully to event {event.name}', 'success')
    return redirect(url_for('dashboard'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':

        user = User.query.filter_by(username=request.form.get('username')).first()
        old_password = request.form.get('old_password')

        if bcrypt.check_password_hash(user.password, old_password):
            print('ok')
            new_password = request.form.get('new_password')
            password_confirm = request.form.get('new_password_confirm')
            if new_password == password_confirm:
                new_pw_hash = bcrypt.generate_password_hash(new_password)
                user.password = new_pw_hash
                db.session.commit()
                flash('Password changed successfuly.', 'info')
            else:
                flash('Password does not match.')
        else:
            flash('Old password dosen\'t exist.', 'danger')
    return render_template('profile.html')


@app.route('/dashboard')
@login_required
def dashboard():
    events = Event.query.all()
    attendees = current_user.attendees  # Attendee.query.filter_by(user_id=current_user.user_id).all()
    print(events, attendees)
    return render_template('dashboard.html', events=events, attendees=attendees)


@app.route('/disjoin/<int:event_id>')
@login_required
def disjoin(event_id):
    attendee = Attendee.query.filter_by(event_id=event_id).first()
    db.session.delete(attendee)
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/test/<int:id>')
def test(id):
    return f"<h1>{id}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
