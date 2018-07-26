from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    nombre = "Juan"
    return render_template('prueba.html', nombre=nombre)


@app.route('/ws/getAll', methods=['GET','POST'])
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
    app.run()
