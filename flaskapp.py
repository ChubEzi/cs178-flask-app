# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        # Extract form data
        title = request.form["title"]
        year = request.form["year"]
        genre = request.form["genre"]
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name:", title, ":", "Favorite Genre:", genre)
        
        flash('User added successfully! Huzzah!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_movie.html')

@app.route('/delete-movie',methods=['GET', 'POST'])
def delete_movie():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name to delete:", name)
        
        flash('User deleted successfully! Hoorah!', 'warning') 
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_movie.html')


#@app.route('/display-movie')
#def display_movie():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
 #   users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
#   return render_template('display_movie.html', users = users_list)


#the JOIN function
@app.route('/display-movie')
def display_movies():
    users_list = getMoviesWithGenres()
    return render_template('display_movie.html', users=users_list)



@app.route('/update-movie', methods=['GET', 'POST'])
def update_movie():
    if request.method == 'POST':
        # Get form data
        movie_id = request.form['movie_id']
        name = request.form['name']
        genre = request.form['genre']

        # Update database (replace with your actual db function)
        # Example:
        # updateMovie(movie_id, name, genre)

        print(f"Updating Movie ID {movie_id} Name: {name}, Genre: {genre}")

        flash('Movie updated successfully!', 'success')
        return redirect(url_for('home'))

    else:
        # Show the update form
        return render_template('update_movie.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
