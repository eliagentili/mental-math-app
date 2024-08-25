from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from .forms import SettingsForm
from .utils import generate_operation
import time

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = SettingsForm()
    if form.validate_on_submit():
        session['operation'] = form.operation.data
        session['num_count'] = form.num_count.data
        session['digit_count'] = form.digit_count.data
        session['start_time'] = time.time()
        session['mode'] = request.form.get('mode')
        session['continuous_mode'] = session['mode'] == 'continuous'
        session['operation_str'], session['correct_answer'] = generate_operation(
            form.operation.data, form.num_count.data, form.digit_count.data
        )
        return redirect(url_for('main.quiz'))
    return render_template('index.html', form=form)

@main_bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        elapsed_time = time.time() - session.get('start_time', time.time())
        correct = float(user_answer) == session['correct_answer']
        flash(f"Correct answer! It took you {elapsed_time:.2f} seconds." if correct else "Wrong answer, try again!")
        
        if session.get('continuous_mode'):
            session['operation_str'], session['correct_answer'] = generate_operation(
                session['operation'], session['num_count'], session['digit_count']
            )
            session['start_time'] = time.time()
            return redirect(url_for('main.quiz'))
        
        return redirect(url_for('main.index'))
    
    return render_template('quiz.html', operation=session.get('operation_str'))

@main_bp.route('/end_continuous_mode', methods=['POST'])
def end_continuous_mode():
    session.pop('continuous_mode', None)
    return redirect(url_for('main.index'))