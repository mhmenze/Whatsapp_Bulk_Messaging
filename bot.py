from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from datetime import datetime
import pyautogui as pg
import time
from urllib.parse import quote
import webbrowser as web


app = Flask(__name__)
app.config['SECRET_KEY'] = '123'  # Change this to a secret key

class UploadForm(FlaskForm):
    numbers_file = FileField('Select numbers file (.csv)')
    message = TextAreaField('Message', validators=[DataRequired()])  # Add StringField for message input
    submit = SubmitField('Send Messages')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    #
    display = ""
    #
    if form.validate_on_submit():
        if form.numbers_file.data:
            numbers_file = form.numbers_file.data
            numbers = numbers_file.stream.readlines()

            current_time = datetime.now()
            hrs = current_time.hour
            mins = current_time.minute
            internet_speed = ""

            # Get the message entered in the text field
            message = form.message.data
            parsed_message = quote(message)

            # Check if the submit button was pressed to send messages
            if form.submit.data:
                internet_speed = "Medium"

                if(internet_speed=="Fast"):
                    waiting = 15
                elif (internet_speed=="Medium"):
                    waiting = 30
                else:
                    waiting = 60

                for i, number in enumerate(numbers):
                    phone = number.decode('utf-8').strip()  # Decode bytes to string and remove newline characters
                    #
                    display = f"{i+1} - {phone} | "
                    print(display, end='')
                    if mins < 59:
                        mins = mins + 1
                    else:
                        hrs = (hrs + 1) % 24  # Reset hours to 0 after reaching 24
                        mins = 0
                    try:
                        phone_no=f"+{phone}"
                        web.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + parsed_message)
                        time.sleep(waiting)
                        width, height = pg.size()
                        pg.click(width / 2, height / 2)
                        time.sleep(waiting-10)
                        pg.press('enter')
                        time.sleep(4)
                        pg.hotkey("ctrl","w")
                        time.sleep(0.5)
                        print("---> Success !")
                        #
                        # display.append("---> Success !<br>")
                    except Exception as e:
                        print(f"Error sending message to {phone}: {e}")
                        #
                        display.append(f"Error sending message to {phone}: {e}<br>")

                return "Messages sent successfully!"

    return render_template("index.html", form=form, display=display)

if __name__ == '__main__':
    app.run(debug=True)
