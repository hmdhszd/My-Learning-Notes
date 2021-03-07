virtualenv -p python3 --no-site-packages --distribute .env       or      virtualenv -p python3 env



source .env/bin/activate


add "django" into this text file :          echo django >> requirements.txt


install django:                             pip3 install -r requirements.txt
show the version of django:                 python3 -m django --version


____________________________________________________________________________________



django-admin startproject mysite


tree mysite


cd mysite/


python manage.py runserver


http://127.0.0.1:8000/


____________________________________________________________________________________



python manage.py startapp polls





polls/views.py  :

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")





polls/urls.py  :

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]







mysite/urls.py  :

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]





python manage.py runserver






____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________





settings.py





# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',







____________________________________________________________________________________


____________________________________________________________________________________



polls/models.py




from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField( max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    vote = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text
    





____________________________________________________________________________________

____________________________________________________________________________________

_________________________________________________________________________________

____________________________________________________________________________________






./manage.py makemigrations 
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model choice






./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK













____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________












./manage.py shell



from polls.models import Question , Choice
from django.utils import timezone

q = Question(question_text = "what about next session?" , pub_date = timezone.now())
q.save()






q.id
1

q.question_text
'what about next session?'

q.pub_date
datetime.datetime(2020, 3, 20, 9, 44, 37, 423344, tzinfo=<UTC>)

Question.objects.filter(question_text__startswith="w")
<QuerySet [<Question: what about next session?>]>

Question.objects.all()
<QuerySet [<Question: what about next session?>]>

Question.objects.filter(id=1)
<QuerySet [<Question: what about next session?>]>







q = Question.objects.get(pk=1)
q
<Question: what about next session?>



q = Question.objects.get(id=1)
q
<Question: what about next session?>










>>> q.choice_set.create(choice_text="online???", vote=0)
<Choice: online???>
>>> 
>>> q.choice_set.create(choice_text="in the park?????", vote=0)
<Choice: in the park?????>
>>> 
>>> q.choice_set.create(choice_text="in the zooooo????", vote=0)
<Choice: in the zooooo????>
>>> 
>>> 
>>> q.choice_set.create(choice_text="at home?????", vote=0)
<Choice: at home?????>



>>> q.choice_set.all()
<QuerySet [<Choice: online???>, <Choice: in the park?????>, <Choice: in the zooooo????>, <Choice: at home?????>]>



>>> q.choice_set.count()
4





















____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

./manage.py createsuperuser




polls/admin.py 



from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)


















____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________



polls/urls.py  :


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]









____________________________________________________________________________________


polls/views.py







from django.http import HttpResponse
from .models import Question,Choice



def index(request):
    output = "output :   "
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ' , '.join([q.question_text for q in last_question_list])
    return HttpResponse(output)



def detail(request,question_id):
    return HttpResponse("you are looking ad the question : {} , {}".format(question_id, Question.objects.get(pk=question_id)))

def result(request,question_id):
    return HttpResponse("result of question {} is : YES ".format(question_id))

def vote(request,question_id):
    return HttpResponse("you are voting to question {}".format(question_id))























____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________


mkdir -p polls/templates/polls
touch polls/templates/polls/index.html





<!DOCTYPE HTML>
<html>
    <body>

    {% if last_question_list %}
        <ul>
            {% for question in last_question_list %}
                <li>
                    <a href="{{question.id}}">{{question.question_text}}</a>
                </li>
            {% endfor %}
        </ul>
    {% endif %}
    </body>
</html>




























____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________


polls/views.py







from django.http import HttpResponse
from .models import Question,Choice
from django.shortcuts import render




def index(request):
    output = "output :   "
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ' , '.join([q.question_text for q in last_question_list])
    #return HttpResponse(output)
    context={
        'last_question_list' : last_question_list,
    }
    return render(request, 'polls/index.html', context)





def detail(request,question_id):
    return HttpResponse("you are looking ad the question : {} , {}".format(question_id, Question.objects.get(pk=question_id)))





def result(request,question_id):
    return HttpResponse("result of question {} is : YES ".format(question_id))





def vote(request,question_id):
    return HttpResponse("you are voting to question {}".format(question_id))














____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________













