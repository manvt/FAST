from flask import render_template,request,Blueprint
from grips_fast.models import Feasibility

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    feasibility = Feasibility.query.order_by(Feasibility.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',feasibility=feasibility)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')

@core.route('/contact_team')
def contact_team():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('contact_team.html')