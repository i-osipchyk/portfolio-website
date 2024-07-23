from flask import current_app as app, render_template, abort


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/project/<project_name>')
def project(project_name):
    return render_template(f'{project_name}.html')
