# Simple Blog Post Application

A responsive and user-friendly Flask-based blog application where users can create, update, like, and delete blog posts. This project is designed to showcase basic CRUD operations and frontend-backend integration.

---

## **Features**

### Frontend:
- Responsive layout with attractive CSS styling.
- Buttons for liking, editing, and deleting posts.
- User-friendly interface for creating and updating posts.

### Backend:
- Flask framework for seamless backend logic.
- Support for all CRUD operations.
- JSON-based storage for blog post data.

---

## **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/F-Fleron-G/Basic-Flask-Module.git

2. Navigate to the project directory:
   ```bash
   cd Basic-Flask-Module

3. Run the application: 
   ```bash
   python3 app.py

4. Open the application in your browser at:
   
   http://127.0.0.1:5000
 
---

## **Usage**
- Home Page: Displays a list of blog posts.
- Add Post: Click "Add Post" to create a new blog post.
- Update Post: Click the edit icon to update an existing post.
- Like Post: Click the like button to increment the like count.
- Delete Post: Click the delete button to remove a post.

---

## **Project Structure**

```plaintext

├── app.py                # Flask application logic
├── blog_posts.json       # Data storage for blog posts
├── static/
│   └── style.css         # CSS styling for the application
├── templates/
│   ├── add.html          # Page for adding a new blog post
│   ├── index.html        # Home page
│   └── update.html       # Page for updating a blog post
└── README.md             # Project documentation

```
---

## **License** 

This project is open-source and available under the MIT License.

