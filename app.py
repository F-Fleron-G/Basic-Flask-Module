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


if __name__ == '__main__':
    """
    Starts the Flask development server.
    The app runs on localhost and port 5000 with debug mode enabled.
    """
    app.run(host="0.0.0.0", port=5000, debug=True)
