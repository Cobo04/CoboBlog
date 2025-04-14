# CoboBlog 📝
### An open-source blog server created by Cohen Schulz, 2025
CoboBlog is written in Python and html, making use of the [Flask library](https://flask.palletsprojects.com/en/stable/) to host the web server. Below are the instructions to administrate the website once it is running.
> [!NOTE]
> The active implementation at [blog.cobored.com](https://blog.cobored.com/) is only managable by those with login credentials.

## Create, Delete, and Manage Accounts 🏂
CoboBlog gives administrators the opportunity to utilize accounts as they see fit. For simplicity, those with a login are able to administrate the entire website. This includes adding and deleting posts and accounts.
### First Time Startup ⚙️
1. Navigate to ☰ -> Login
   - Username: ```admin```
   - Password: ```admin```
2. Once redirected to the home page, navigate to ☰ -> Register and enter the desired login info for the administrator account.
> [!CAUTION]
> It is absolutely crucial that you follow the next steps. Failure to do so will allow virtually anyone to login to the website.
3. Navigate to ☰ -> Users
   - **Delete** the ```admin``` account to ensure that the dummy login info is removed.
> [!TIP]
> If all accounts are deleted by accident, the ```admin``` account will be created automatically upon server restart.

## Add and Delete Blog Posts 😎
The heart and soul of CoboBlog is the ability to construct detailed, managable posts that support a diverse backgroud of information.
### The Anatomy of a Post 🙅
Every post on CoboBlog contains the following information:
- **Title**: A title for your post. It is displayed on the index page card, as well as the individual post page, both utilizing ```display``` classes from CSS's [Bootsrap](https://getbootstrap.com/).
- **Content**: The main article content. Blogs on CoboBlog **REQUIRE** a distinct format to be displayed properly. Follow the steps below to have your post live up to the gold-standard.
- **Description**: A short summary of the article, *only 2-3 sentences long*. Give the viewer a brief overview of what is to come.
- **Authors**: The contributors of the article. Follow the format below.
- **Post Type**: A blog on CoboBlog can be one of 4 types: ```Proof```, ```Writing```, ```Personal```, and ```Other```. Select the type that makes the most sense for your article, following the descriptions below.
  - ```Proof```: A mathematical post.
  - ```Writing```: An essay or academic publicaton outside of the realm of mathematics.
  - ```Personal```: A life update, or anything relating to you in particular. Opinions, promulgations, and statements would all fall into this category.
  - ```Other```: Anything that doesn't fall into the categories above.

### Create a Post 🗿
1. Navigate to ☰ -> New Blog and input the following information
