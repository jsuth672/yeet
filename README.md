# cps420-project-y-e-e-t

requirments:

python
<br>django
<br>docker
<br>
<br>
**step 1**: clone repository
<br>
**step 2**: run 'docker-compose up' in the repo<br>
**step 3**: in a browser go to http://localhost:8080
<br>username: user@example.com
<br>password: password
<br>**step 4**: create a server
<br>Host: db
<br>Port: 5432
<br>User: postgres
<br>Pass: postgres
<br>**step 5**: create a database named 'polls'
<br>**step 6**: run the command 'python manage.py migrate' inside the mysite directory
<br>
<br> We have not yet figured out how to send the database with the program. Therefore, the following steps will set up a simple poll.

<br>**step 7**: inside the mysite directory, run 'python manage.py shell'
<br>**step 8**: copy and paste the following lines:
<br>
<br>from django.utils import timezone
<br>from polls.models import Choice, Question
<br>q = Question(question_text="Stage 1: init",question_assigned="YEET", pub_date=timezone.now())
<br>q.save()
<br>q.choice_set.create(choice_text='will do', votes=0)
<br>q.choice_set.create(choice_text='working', votes=0)
<br>q.choice_set.create(choice_text='done', votes=0)
<br>q.save()
<br>
<br>
<br>**step 9**: run "python manage.py runserver" in the mysite directory
<br>**step 10**: go to http://localhost:8000/polls to use the polls

<br> ***the extra field we added was an assinged name to every poll (i.e. task)***