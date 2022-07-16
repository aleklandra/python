from flask import Flask
from flasck import render_template

from vsearch import search_for_letters

app = Flask(__name__)

@app.route('/')

def hello() -> str:
    return 'Hello world from Flask!'
    
@app.route('/search')

def do_search() -> str:
    return str(search_for_letters('Hello world'))
    
@app.route('/entry')
    
def entry_page()-> 'html':
    return render_template('entry.html', the_title='Welcom to my web-app!')



app.run()
