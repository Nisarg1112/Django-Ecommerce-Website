# ⚡️ Django E-commerce Website

I made this personal project during my summer vacation as I was learning new stuff so!.

**Technology Stack used :**<br>

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" > <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" >  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" > <img src="https://img.shields.io/badge/redis-CC0000.svg?&style=for-the-badge&logo=redis&logoColor=white" > <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" >

## ⚡️ Main Features

<ul type='round'>
<li>Admin can list the categories, brands and their related products. <br>I used <strong>django-mptt</strong> model which a Tree like data structure to implement relationship between category, brand and it's product smoothly.</li> 
<li>Admin can list the products-details, price and quantity they have for that specific product.<br>
I used <strong>ckeditor</strong> which is a <strong>rich text editor</strong>, It gives us advantage over normal text editor for writing product specifications.</li>

<li>admin can see the details of ordered items, and can mark the order as <i>'confirmed'</i> or <i>'shipped'</i> or <i>'delivered'</i>. </li>
<li>User can Sign In or Sign Up easily.</li>
<li>Implemented Search product functionality, User can search their product in real time, It is being done using <strong>AJAX requests</strong>.</li>
<li>Category wise filter is given, user can shop with brands of specific category also.
User can add product to their cart directly from home page or product detail page.</li>
<li>User can see their cart price and number of products in cart updates as they shop. At shop cart page user can see full shop cart with detailed price and Final Price (with 18% GST).</li>
<li>On pressing the Place Order button the user would see order confirmation message with Order No., If their order is successfully placed.</li>
<li>In background, <strong>Celery will send an Email Asynchronously using Redis server</strong> to desired mail id with order confirmation message, Order No. and automatically generated pdf of bill. I used <strong>Jinja templates</strong> to automate the process of generating bill receipt.</li>
</ul>

## ⚡️ How to Use


Just follow 4 simple steps:

1. Clone repository to preserve directory structure<br>
`git clone https://github.com/Nisarg1112/Django-Ecommerce-Website.git`
2. Go to your favorite code editor and open Command Prompt (cmd) amd go to directory where you cloned this repo
3. Run this command in cmd<br>
   `pip install -r requirements.txt`
4. Extract `Redis-x64-3.0.504.zip`
5. Run the file `redis-server.exe`
6. Run the file for command line access of Redis server `redis-cli.exe`
7. If you see this on Redis command line 
   `redis 127.0.0.1:6379>` then,
   type `PING` and hit Enter.
8. You should see output as `PONG`. If that's the case then now you are good to go!
8. Open cmd and write following commands<br>
   `cd mac`
9.  following command will perform required migrations
   `python manage.py migrate`
11. following command will start a local server
   `python manage.py runserver`
11. Now, We are all set to go! Enjoyy😎!
   
## 🙋‍♂️ Helpdesk

**If you face any problem like script not running in local environment or anything:** You can reach out to me at anytime on following platforms!
<br>
<br>
<a href="mailto:nisargtrivedi054@gmail.com" target="_blank"> <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" title="Send a Mail to Nisarg Trivedi"></a> <a href="https://www.linkedin.com/in/nisargtrivedi1112" target="_blank"> <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" title="Reach out to Nisarg Trivedi"></a>

## ℹ References

<ul type='square'>
  <li><strong>Celery Official Documentation - </strong><a href='https://docs.celeryproject.org/en/stable/'>You can find here</a></li>
  <li><strong>Redis for Python Official Documentation - </strong><a href='https://pypi.org/project/redis/'>You can find here</a></li>
  <li><strong>The official Redis </strong><a href='https://redis.io/documentation'>website</a></a></li>
  <li><strong>Redis-x64-3.0.504.zip </strong> has been downloaded from <a href='https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504'>here</a></a></li>
  <li><strong>Django Official Documentation - </strong><a href='https://docs.djangoproject.com/en/3.2/'>You can find here</a></li>
  <li><strong>django-mptt Official Documentation - </strong><a href='https://django-mptt.readthedocs.io/en/latest/'>You can find here</a></li>
  <li><strong>ckeditor - <i>rich text editor</i> Official Documentation - </strong><a href='https://django-ckeditor.readthedocs.io/en/latest/'>You can find here</a></li>
</ul>
