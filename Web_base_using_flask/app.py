from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

app = Flask(__name__)
app.secret_key = "BSU Lipa"

class Login(FlaskForm):
    g_suite = StringField('G-Suite Account: ', validators=[DataRequired(), Length(min=1, max=50)])
    sr_code = StringField('SR-Code: ', validators=[DataRequired(), Regexp(r'^\d{2}-\d{5}$')])
    submit = SubmitField('Submit')

@app.route('/loginStudent', methods=['GET', 'POST'])
def loginStudent():
    form = Login()
    if form.validate_on_submit():
        g_suite = form.g_suite.data
        sr_code = form.sr_code.data
        return "Login Successfully! Welcome to Library of BSU LIPA."
    return render_template("LoginStudent.html", form=form)


@app.route('/about')
def about():
    return render_template('AboutUs.html')

class Admin(FlaskForm):
    adminEmail = StringField('Admin Email: ', validators=[DataRequired(), Length(min=1,max=20)])
    adminPassword = PasswordField('Admin Password: ', validators=[DataRequired(), Length(min=1,max=20)])
    submit = SubmitField('Login')

@app.route('/loginAdmin', methods=['GET','POST'])
def loginAdmin():
    form = Admin()
    if form.validate_on_submit():
        adminEmail = form.adminEmail.data
        adminPassword = form.adminPassword.data
        if adminEmail == "Admin123" & adminPassword == "AdminPassword":
            return "Successfully Login!"
        else:
            return "Invalid credentials"
    return render_template("LoginAdmin.html", form=form)


@app.route('/')
def index():
    return render_template("Homepage.html")

if __name__ == '__main__':
    app.run(debug=True)
