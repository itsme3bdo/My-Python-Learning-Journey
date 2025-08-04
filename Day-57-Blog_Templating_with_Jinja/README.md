Blog Templating with Jinja
My First Blog with Dynamic Content

This is a personal milestone where I built my very first blog using Flask and Jinja2 templates. The goal of this project was to create a clean, functional blog that could dynamically display blog posts from an external data source. I learned how to combine the power of a web server with templating to generate a full website from a single template and a list of data.

How It Works 

Flask: I used the Flask framework to set up a basic web server. It's lightweight and makes it easy to get a web application up and running quickly.

Templates: I used Jinja2 templating to create a reusable HTML layout for the blog. This allowed me to create a single template that could display multiple blog posts dynamically.

Dynamic Data: I used the requests module to fetch a list of blog posts from an external API. This is a great way to handle dynamic content, as the website can be updated just by changing the data source.

Routing: I used Flask's routing decorators to handle different web requests, such as displaying the main blog page and a specific page for each blog post.
