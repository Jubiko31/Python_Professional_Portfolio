from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from db import db
from models.cafe import CafeModel
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')
    
@app.before_first_request
def create_table():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    cafe_list = CafeModel.find_all()
    print(cafe_list)
    return render_template('cafes.html', cafes=cafe_list)

@app.route("/add", methods=["GET", "POST"])
def add_new_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = CafeModel(
            name = request.form.get("cafe"),
            map_url = request.form.get("location"),
            open_time = request.form.get("open"),
            close_time = request.form.get("close"),
            coffee = request.form.get("coffee_rating"),
            wifi = request.form.get("wifi_rating"),
            power = request.form.get("power_rating"),
        )
        CafeModel.save_to_db(cafe)
        return redirect(url_for("cafes.html"))
    return render_template('add.html', form=form)

@app.route("/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = CafeModel.find_by_id(cafe_id)
    if cafe:
        CafeModel.delete_cafe(cafe)
        return jsonify(response={"success": "Cafe deleted successfully."}), 200
    else:
        return jsonify(error={"Not Found": "Invalid cafe ID."}), 404

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=3333, debug=True)
