from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class LeadForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Regexp('^[a-zA-Z]+$', message='Only alphabets allowed')])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email format')])
    phone_number = StringField('Phone Number', validators=[InputRequired(), Regexp('^[0-9]{10}$', message='Invalid Indian phone number')])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=12), Regexp('^[a-zA-Z0-9!@#$%^&*()_+]+$',
                                                                                           message='Invalid password format')])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(max=12), Regexp('^[a-zA-Z0-9!@#$%^&*()_+]+$',
                                                                                                       message='Invalid password format')])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def lead_form():
    form = LeadForm()

    if form.validate_on_submit():
        # printing to console
        print("Lead Information:")
        print(f"Name: {form.name.data}")
        print(f"Email: {form.email.data}")
        print(f"Phone Number: {form.phone_number.data}")
        print(f"Password: {form.password.data}")
        # printing on screen on submit
        return "submitted successfully!" \
               f"\n Name: {form.name.data} " \
               f"\n Email: {form.email.data}"

    return render_template('lead_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
