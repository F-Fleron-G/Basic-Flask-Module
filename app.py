from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def load_posts():
    """
    Loads all blog posts from the JSON file.
    Returns:
        list: A list of dictionaries representing the blog posts
    """
    with open("blog_posts.json", "r") as file:
        return json.load(file)


def save_posts(posts):
    """
    Saves the current list of blog posts to the JSON file.
    Args:
        posts (list): The list of blog posts to save.
    """
    with open("blog_posts.json", "w") as file:
        json.dump(posts, file, indent=4)


def fetch_post_by_id(post_id):
    blog_posts = load_posts()
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


@app.route('/')
def index():
    """
    The home page route. It fetches all the blog posts and renders them
    on the index.html template.
    Returns:
        Response: The rendered home page template.
    """
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    The route for adding a new blog post. On GET requests, renders a form
    to add a post. On POST requests, it processes the form data, adds a new
    post, and saves it to JSON file.

    Returns:
        Response: The rendered add.html template or a redirect to the home page.
    """
    if request.method == "POST":
        blog_posts = load_posts()

        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        new_id = max(post["id"] for post in blog_posts) + 1 if blog_posts else 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content
        }

        blog_posts.append(new_post)
        save_posts(blog_posts)

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handles updating an existing blog post.

    When you visit this route with a specific post ID:
      - On a GET request, it shows the update form pre-filled with the current
        details of the blog post.
      - On a POST request, it saves the updated details (like the title and content)
        back to the list of blog posts and updates the JSON file.

    Args:
        post_id (int): The unique ID of the blog post you want to update.

    Returns:
        Response:
            - Renders the update.html template for GET requests.
            - Redirects to the home page once the post is successfully updated.

    Note:
        If the post with the given ID isn't found, you'll get a "Post not found"
        message with a 404 status code.
    """
    blog_posts = load_posts()

    post = next((p for p in blog_posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')

        save_posts(blog_posts)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """
    The route for deleting a blog post. Removes the post with the specified
    ID from the list blog posts and saves the updated list to the JSON file.

    Args:
        post_id (int): The ID of the post to delete.

    Returns:
        Response: A redirect to the home page after deletion.
    """
    blog_posts = load_posts()
    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    save_posts(blog_posts)

    return redirect(url_for("index"))


@app.route('/like/<int:post_id>')
def like(post_id):
    """
    Handles the 'Like' action for a blog post.

    Args:
        post_id (int): The unique ID of the blog post to like.

    Returns:
        Response: Redirects back to the home page after incrementing the like count.
    """
    blog_posts = load_posts()

    for post in blog_posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break

    save_posts(blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    """
    Starts the Flask development server.
    The app runs on localhost and port 5000 with debug mode enabled.
    """
    app.run(host="0.0.0.0", port=5000, debug=True)
