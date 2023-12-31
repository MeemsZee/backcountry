# Backcountry Series Website
#### Video Demo:  <https://youtu.be/l7BFuzGwEwI>
#### Description: Create blog like website for campers and climbers

#### Purpose of website
This website serves as a lifestyle blog to document and share my nomadic life. This website is for people who want to learn about what it takes to live life on the road. 
It is for tips on how to live more comfortably in small spaces, how to get the most out of trips and reviews on places I have been to. 

#### API choices
* Flask - to streamline the website making process.  This is used with python
    * Session - important so admin can make changes to the database
* SQLAlchemy - this ORM was chosen for it's ability to create classes and query databases easily. 
* Mistune - used to convert MD to html.  Post content is saved in the database as markdown. 
* Sqlite3 - this is the database used to store post information for the website. It is compatible with SQLAlchemy and queries for the page is simple so there is no need for a more user friendly DB.
* ToastUI editor - This editor allows content to be saved as MD and makes saving into databases easier.   

#### Database 
The file website.db has two tables: user and posts.  
* User - This table has an id number column as its primary key, username, password that is hashed before storing in the database, and created at column.  I suspect hashing the password isn't the most secure way to store passwords, so if in the future there are actual users besides admin a new method will be required. 
* Posts - This table has an id number column as its primary key, category, title, tages, pic_path, content, and created at column.  
    * Categories - climbing, cooking and trailer.  These are the only options available to pick from in the form. 
    * Title - up to 140 characters are allowed for each entry
    * Content - content is saved in MD language by using the toastui api. 

#### app.py
* def index() and def backcountry():
    *brings you to the homepage

* def trailer(), def cooking(), def climbing(): 
    * queries into database to filter all entries by their respective category and stored as a list
    * once list is populated, the respective html page will be rendered

* def all_post(post_id):
    * app.route is "/post_<int:post_id>/" - this means the route of each post is "/post_" plus the post_id pulled from the database
    * id is pulled from the Post table according filtered by post_id.  it returns the row corresponding to the post_id number
    * md_to_html holds the values of the contents column from the id variable. Mistune is used to convert md to html before rendering post-page.html

* def about():
    * renders about.html

* def post():
    * if method is post, commit form to the Post table and then you are redirected to the homepage.  Redirection can be changed in the future, maybe to the actual post page
    * if method is get, garage.html will be rendered
    * the name garage is picked as a psuedo-name for admin to make it harder for bad actors to find since this is an admin only page

* def edit(post_id):
    * app.route is "/post_<int:post_id>/edit/" - this means the route of each post is "/post_" plus the post_id pulled from the database plus /edit/
    * first the post is pulled from the database and stored as such
    * if the method is post, commit the post to the database.  SQLAlchemy will update the entry
    * then admin will be redirected to the corresponding post_id page
    * if the method is get, edit.html will be rendered

* def delete(post_id):
    * app.route is "/post_<int:post_id>/edit/" - this means the route of each post is "/post_" plus the post_id pulled from the database plus /delete/
    * deletes from the Post table the entry with the corresponding post_id
    * after delection, redirect to editable.html

* def editable():
    * pulls all entries from the Post table
    * renders editable.html

* def login():
    * clear all sessions
    * if method is post, make sure the username and password for the admin is correct  
    * no other sessions are possible 
    * render garage.html
    * if method is get, render login.html

* def register():
    * if method is post, commit the username and password to the User table
    * if method is get, render register.html

* def logout():
    * clear the current session and then redirect to index 

#### Pages content/HTML files
* Overall Note: 
    * All pages are responsive.
* Navbar: 
    * The navbar is provied by bootstrap 5 with a few css changes. 
    * When width of navbar can't accommodate name of links, the hamburger will appear with the links listed 
* Index:
    * This is the main page where readers get a glimpse of what they can expect from my page.  I decided to place a flashy background to entice readers.  In the body of the page, 
there are 3 boxes with links to other pages and a quick description of the contents of those page. 
* Trailer Life, Small Kitchen Cooking, Climbing:
    * These pages contains a list in grid form of existing posts.  Each Grid has a title and a snippet of the post.
    * .truncate in the css style sheet shortens the contents of the post into 2 lines and adds "..." to the end of it 
    * Two media queries are created so the page can accommodate different screen sizes from a pc or laptop to the iphone SE
* Posts:
    * Each post will have their own page with a title, and the contents of the post. 
* About:
    * A quick intro of me and why I created the website.
* Admin pages:
    * These pages are accessible to admins only.  There will be login and log out links. Below are the functionalities of the pages. All pages should have a log out link
        * Garage - This page is to create and submit posts
            * Admin can pick which category the post will be under 
            * all other inputs are texts
            * ToastUI editor is utilized. For more information, go to their documentation.  On change of anything in the box, content (hidden) will be updated. Left part of the divider is MD and the right side is the how it will look on a website
        * Editable - This page has a list of all of the posts with the option to delete or edit them
            * Delete will prompt the user to confirm they want the post deleted
        * Post-tools - This page is to edit existing posts
            * it will look very much like /garage except that admin will have the contents of the post populated into the input boxes
* Login - This page allows admin to login.  One is able to register, but as of now, a registered user has no functionality. This is for the future if it is decided that commentors can created their own username to post on the page. The information is stored in a database. Currently, if the username or password isn't correct, garage.html will be rendered, in which admin should try again to login with correct credentials.

 #### Future additions/updates: 
* Search bar - this would sit at the navbar.  Figure out how to create one.  Ideally, it will pull up links for users
* Enable comments from visitors 
    * Create a comments table to store the comments and from which user
    * Should it be like how google does it, where anonymous users can post and get assigned an animal? 
* Backcountry series website to be up and running
    * The domain name has been bought. 
    * Figure out which service to use in order to host the website.  Should be a free one since storage for the time being isn't large
* Optimize list of posts pages:
    * loading time is an issue since all the contents are loaded to the page, but is hidden via the truncation
    * Should the Post table include a truncated version of the content? currently with the layout, it may be the most viable method, unless there is a way to append to each entry after querying all posts
* Redirecting after creating a post to the post page.  Currently it redirects to the index.  Not the biggest deal since it is on the admin side and not user
* Update the login page to show errors if password or username is incorrect
* Register page - Create errors letting client knows if there are any issues
* See if adding a thumbnail photo for each post listing makes the page look put together. Or at least find a way to make it look better.  Figure out how to crop pics to fit into the listing's width
* Change the css for post pages to make content look better. 
    * Right now the photos and the words of the posts aren't the most asthetically pleasing.
* Make sure User table has only unique users.  I have done this before in the past. Should be easy to do. 
* Make the category tab show the actual category of the post on edit pages.  Right now you have to pick the category all over again. 

