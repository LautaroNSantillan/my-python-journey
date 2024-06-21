from flask import Flask,render_template, request, redirect, url_for
from forms import Todo
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os


class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

project_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(project_dir, 'tmp', 'test.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"


app.config['SECRET_KEY'] = 'pwd'

db.init_app(app)


class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    def __str__(self):
        return f'{self.content}, {self.id}'



@app.route('/', methods=['GET', 'POST'])
def hello_world():
    req_method = request.method
    todos = TodoModel.query.all()
    if req_method == 'POST':
        first_name = request.form['first_name']
        return redirect(url_for("name", first_name=first_name))
    return render_template('req.html', request_method=req_method, todos=todos)


@app.route('/name/<string:first_name>')
def name(first_name):
    return f'{first_name}'


@app.route('/todo',methods=['GET', 'POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        todo = TodoModel(content=todo_form.content.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('todo.html', form=todo_form)


if __name__ == '__main__':
    # from flask: This requires an application context. Since you’re not in a request at this point, create one manually.
    with app.app_context():
        db.create_all()
        print("Database tables created.")
    app.run(debug=True)  # production : false

# on Pyhton shell to persist a todo:
# >>> from app import app, db, TodoModel
# >>> with app.app_context():
# ...     new_todo = TodoModel(content="Sample Todo")
# ...     db.session.add(new_todo)
# ...     db.session.commit()
# ...     print("Todo added:", new_todo)
