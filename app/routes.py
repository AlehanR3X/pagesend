from flask import Blueprint, render_template, request, redirect, url_for, flash
from .utils.telegram_utils import send_message  # Importación relativa a la carpeta app

app = Blueprint('app', __name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        target_chat = request.form.get('target_chat')
        message = request.form.get('message')
        if target_chat and message:
            try:
                send_message(target_chat, message)  # Function to send message
                flash('Message sent successfully!', 'success')
            except Exception as e:
                flash(f'Error sending message: {str(e)}', 'danger')
            return redirect(url_for('app.send'))
    return render_template('send.html')