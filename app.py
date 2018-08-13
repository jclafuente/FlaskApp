#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    nombre = "Index"
    return render_template('prueba.html', nombre=nombre)


@app.route('/params')
def params():
    # Parametros en el request tipo GET
    parm = request.args.get('param1', 'no contiene este parametro')

    nombre = "El parametro es : {}".format(parm)
    return render_template('prueba.html', nombre=nombre)


@app.route('/ws/getAll', methods=['GET', 'POST'])
def get_all():
    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5656)
