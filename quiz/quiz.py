#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#  
#  Copyright 2020 Gaming <Gaming@GAMING-PC>
#  

from flask import request, redirect, url_for, flash
from flask import Flask
from flask import render_template

app = Flask(__name__)
 
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'}, 
    {
    'pytanie': 'ile nóg ma kulawa ośmiornica?:',
    'odpowiedzi': ['8', '7', '1'],
    'odpok': '8'},
]


 
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', pytania=DANE)

@app.route('/Wynik', methods=['GET', 'POST'])
def odpowiedzi():
    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form
        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1
        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('odpowiedzi'))
    return render_template('Wynik.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)
