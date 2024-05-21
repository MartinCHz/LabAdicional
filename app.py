# Cree una aplicación utilizando FLask donde maneje un CRUD básico de la información de una persona.  
# Haga todas las funcionalidades con su lógica completa
# Haga una lista de 5 persons con sus respectivos datos inicialmente. 
# Haga los botones de agregar, modificar y eliminar una persona funcionen.
# Los campos de la entidad estudiante es id (según la longitud de la lista), name, email, age.
# Sus endpoints son /add, /edit y /delete. 
# Trabaje con listas y los templates creados add.html, edit.html y index.html
# Defina las funciones como add, edit y delete.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

persons = [
    {'id': 1, 'name': 'John', 'email': 'john@example.com', 'age': 30},
    {'id': 2, 'name': 'Jane', 'email': 'jane@example.com', 'age': 25},
    {'id': 3, 'name': 'Bob', 'email': 'bob@example.com', 'age': 40},
    {'id': 4, 'name': 'Alice', 'email': 'alice@example.com', 'age': 35},
    {'id': 5, 'name': 'David', 'email': 'david@example.com', 'age': 28}
]

@app.route('/')
def index():
    return render_template('index.html', persons=persons)

@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        new_person = {'id': len(persons) + 1, 'name': request.form['name'], 'email': request.form['email'], 'age': request.form['age']}
        persons.append(new_person)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    person  = next((p for p in persons if p['id'] == id), None)  
    if request.method == 'POST':
        person['name'] = request.form['name']
        person['email'] = request.form['email']
        person['age'] = request.form['age']

        return redirect(url_for('index'))
    return render_template('edit.html')

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    person  = next((p for p in persons if p['id'] == id), None)
    if request.method == 'POST':
        persons.remove(person)
        return redirect(url_for('index'))
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)