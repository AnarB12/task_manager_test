from flask import Blueprint, render_template, redirect, url_for, request, abort, flash
from flask_login import login_required, current_user
from .models import Task
from .forms import TaskForm, EditTaskForm, SearchForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = SearchForm()
    if form.validate_on_submit():
        search_term = form.search.data
        return redirect(url_for('main.search_results', query=search_term))
    page = request.args.get('page', 1, type=int)
    tasks = Task.query.filter_by(author=current_user).order_by(Task.timestamp.desc()).paginate(page=page, per_page=5)
    return render_template('tasks.html', tasks=tasks, form=form)

@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            author=current_user
        )
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('main.tasks'))
    return render_template('new_task.html', form=form)

@main.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        abort(403)
    form = EditTaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        task.is_complete = form.is_complete.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.tasks'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.due_date.data = task.due_date
        form.is_complete.data = task.is_complete
    return render_template('edit_task.html', form=form)

@main.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.tasks'))

@main.route('/search_results/<query>')
@login_required
def search_results(query):
    tasks = Task.query.filter(
        Task.author == current_user,
        (Task.title.ilike(f'%{query}%')) | (Task.description.ilike(f'%{query}%'))
    ).all()
    return render_template('search_results.html', tasks=tasks, query=query)
