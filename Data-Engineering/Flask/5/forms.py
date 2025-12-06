from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        flash(f'Registration successful for {email}!', 'success')

        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return 'Registration Successful!'

if __name__ == '__main__':
    app.run(debug=True)

