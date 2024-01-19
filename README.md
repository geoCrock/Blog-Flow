# Blog-Flow

BlogFlow is a user-friendly and intuitive web portal designed for creative individuals who want to share their thoughts and ideas with the world. Our project provides a simple and effective tool for creating, editing and managing your blog posts.

Peculiarities:

- Post Creation: An intuitive form of post creation that allows you to freely express your thoughts and ideas.
- Editing posts: Ability to make changes to already published posts, keeping the content relevant.
- Post Management: Simple interface to manage your posts, including deleting, editing and tracking statistics.
- Likes and feedback: The ability to receive feedback from readers in the form of likes and comments.
- Blog-Flow is designed to keep your creative flow uninterrupted. Share your stories, opinions and experiences with the world using BlogFlow - your ideal blogging partner.

## Launch

1. Copy the repository:

      ```bash
      git clone https://github.com/geoCrock/Blog-Flow.git
      ```

2. Create `venv` and install dependencies:

      ```bash
      python -m venv venv
      ```
      or

      ```bash
      source venv/bin/activate
      ```
     
      ```bash
      pip install -r requirements.txt
      ```

3. Make migrations and run the project:
   
     ```bash
     python manage.py makemigrations
      ```

     ```bash
     python manage.py migrate
      ```

     ```bash
     python manage.py runserver
      ```


## Running via Docker

Make sure the following components are installed on your system:

- Docker
- Docker Compose


1. Copy the repository:

      ```bash
      git clone https://github.com/geoCrock/Blog-Flow.git
      ```

2. Create and run Docker containers:

      ```bash
      docker-compose up --build
      ```
