from flask import render_template # import module to render html pages 
from app import app

@app.route('/')
def index():
    '''
    views for the homapage o index page 
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''returns a dynamic link of movie id'''
    return render_template('movie.html', id = movie_id)
