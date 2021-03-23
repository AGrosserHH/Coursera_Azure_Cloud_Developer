from flask import flash, render_template, redirect, request
from FlaskExercise import app
import logging


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    app.logger.warning(log)
    return render_template(
        'index.html',
        log=log
    )
