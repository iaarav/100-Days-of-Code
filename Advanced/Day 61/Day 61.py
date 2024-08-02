from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired(), Length(min=4)])
    password = PasswordField('pass', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "MyForm("
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
