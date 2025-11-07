from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

# Global list to store To Do items
todo_list = []


def is_valid_email(email):
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


@app.route('/')
def index():
    """Main controller - displays To Do list and form"""
    return render_template('index.html', todos=todo_list)


@app.route('/submit', methods=['POST'])
def submit():
    """Controller for submitting new To Do items"""
    # Get form data
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '')

    # Validate email
    if not is_valid_email(email):
        # Redirect back without adding (could add error message here)
        return redirect('/')

    # Validate priority
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Validate task is not empty
    if not task:
        return redirect('/')

    # Add new To Do item to the list
    todo_item = {
        'task': task,
        'email': email,
        'priority': priority
    }
    todo_list.append(todo_item)

    # Redirect back to main page
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    """Controller for clearing all To Do items"""
    global todo_list
    todo_list = []
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)