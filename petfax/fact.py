# from flask import ( Blueprint, render_template, request, redirect, url_for )
# import json

# bp = Blueprint('fact', __name__, url_prefix='/facts')

# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     # print(request.form)
#     return render_template('facts.html')

# @bp.route('/new')
# def new_fact():
#     return 'Here is the fact page!'

# @bp.route('/submit', methods=['POST'])
# def submit_fact():
#     name = request.form['name']
#     fact = request.form['fact']

#     print(f"Name: {name}, Fact: {fact}")
#     return redirect(url_for('fact.new_fact'))

# @bp.route('/')
# def new():
#     return render_template('facts.html')

from flask import ( Blueprint, render_template, request, redirect )
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']
        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()
        return redirect('/facts')
    
    all_facts = models.Fact.query.all()
    return render_template('facts/index.html', facts=all_facts)

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/submit', methods=['POST'])
def submit_fact():
    print(request.form)