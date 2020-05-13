from flask import Blueprint
from flask import render_template, request, Blueprint
from flask_blog.models import Post


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)  # to identify the page number we want
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5,
                                                                  page=page)  # to identify how many posts per page
    return render_template('home.html', posts=posts)




@main.route('/about')
def about():
    return render_template('about.html', title='About')