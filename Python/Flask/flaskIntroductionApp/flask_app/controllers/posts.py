from flask_app import app
from flask import render_template, request, redirect, flash
from flask_app.models.post import Post

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = Post.get_all())

@app.route('/post/new')
def addPost():
    return render_template('addPost.html')

@app.route('/post', methods = ['POST'])
def createPost():
    if len(request.form['title'])< 1 or len(request.form['content'])< 1:
        flash('Ke error. Ploteso te dhenat', 'errorNeKrijimPosti')
        return redirect(request.referrer)
    data = {
        'title': request.form['title'],
        'content': request.form['content']
    }

    Post.save(data)

    return redirect('/posts')

@app.route('/delete/post/<int:id>')
def deletePost(id):
    data = {
        'id': id
    }
    Post.delete(data)
    return redirect(request.referrer)