# school_master
This project to school master to add post and show to all permission 

absl-py==1.4.0
anyio==3.3.1
argon2-cffi==21.1.0
asgiref==3.4.1
attrs==21.2.0
Babel==2.9.1
backcall==0.2.0
backports.entry-points-selectable==1.1.0
bleach==4.1.0
certifi==2021.5.30
cffi==1.14.6
charset-normalizer==2.0.6
colorama==0.4.4
comtypes==1.1.10
contourpy==1.0.7
cycler==0.11.0
debugpy==1.4.3
decorator==5.1.0
defusedxml==0.7.1
distlib==0.3.3
Django==3.2.9
django-qrcode==0.3
djangorestframework==3.12.4
djangorestframework-simplejwt==5.0.0
entrypoints==0.3
environ==1.0
environment==1.0.0
et-xmlfile==1.1.0
filelock==3.3.1
flatbuffers==23.1.21
fonttools==4.38.0
idna==3.2
importlib-resources==5.10.2
ipykernel==6.4.1
ipython==7.27.0
ipython-genutils==0.2.0
ipywidgets==7.6.5
jedi==0.18.0
Jinja2==3.0.1
json5==0.9.6
jsonschema==3.2.0
jupyter==1.0.0
jupyter-client==7.0.3
jupyter-console==6.4.0
jupyter-core==4.8.1
jupyter-server==1.11.0
jupyterlab==3.1.13
jupyterlab-pygments==0.1.2
jupyterlab-server==2.8.1
jupyterlab-widgets==1.0.2
kiwisolver==1.4.4
MarkupSafe==2.0.1
matplotlib==3.7.0
matplotlib-inline==0.1.3
mediapipe==0.9.1.0
mistune==0.8.4
mysql==0.0.3
mysqlclient==2.0.3
nbclassic==0.3.2
nbclient==0.5.4
nbconvert==6.1.0
nbformat==5.1.3
nest-asyncio==1.5.1
notebook==6.4.4
numpy==1.21.2
opencv-contrib-python==4.7.0.68
openpyxl==3.0.10
packaging==21.0
pandas==1.3.3
pandocfilters==1.5.0
parso==0.8.2
pickleshare==0.7.5
Pillow==8.3.2
platformdirs==2.4.0
prometheus-client==0.11.0
prompt-toolkit==3.0.20
protobuf==3.20.3
pycparser==2.20
Pygments==2.10.0
PyJWT==2.3.0
PyMySQL==1.0.2
pyparsing==2.4.7
pypiwin32==223
pyrsistent==0.18.0
python-dateutil==2.8.2
pyttsx3==2.90
pytz==2021.3
pywin32==301
pywinpty==1.1.4
pyzmq==22.3.0
qrcode==7.3.1
qtconsole==5.1.1
QtPy==1.11.2
requests==2.26.0
requests-unixsocket==0.2.0
Send2Trash==1.8.0
six==1.16.0
sniffio==1.2.0
sqlparse==0.4.2
terminado==0.12.1
testpath==0.5.0
tornado==6.1
traitlets==5.1.0
urllib3==1.26.7
virtualenv==20.8.1
wcwidth==0.2.5
webencodings==0.5.1
websocket-client==1.2.1
widgetsnbextension==3.5.1
zipp==3.13.0




Frist  step -

project name-school_master
aapname-users
 Register page - register page make a  class base using  AbstractUser becouse phone is nat a  filed to add this filed to use AbstractUser

 Register page urls- http://127.0.0.1:8000/register/

 class User(AbstractUser):
    name=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(max_length=200,unique=True)
    phone =models.CharField(max_length=10, blank=True, null=True)
    user_type=models.CharField(max_length=10,
                               choices=
                               [
                                   ("admin","admin"),
                                   ("teacher","teacher"),
                                   ("student","student"),
                               ],
                               default='admin')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


  step2 -then  to multiple user to crete a filed a user_type and choices filed

  user_type=models.CharField(max_length=10,
                               choices=
                               [
                                   ("admin","admin"),
                                   ("teacher","teacher"),
                                   ("student","student"),
                               ],
                               default='admin')
  then to register a user as any one id to on a as admin  or teacher or student
  then  user mast be register  and tha  must be impotent at is a admin men user and to show all post
  and with user name to show to admin  and student to to show  only student post and teacher  show to student
  and teacher booth  show to post becouse  i give this parmision.

   if not request.user.is_authenticated:
        return redirect("/login")
    if request.user.user_type == "admin":
        gallery = Gallery.objects.filter()
    if request.user.user_type=="teacher":
        gallery=Gallery.objects.filter(
            Q(Q(user=request.user) | Q(user__user_type='student'))

        )
    if request.user.user_type == "student":
        gallery = Gallery.objects.filter(user=request.user
        )


        urls- http://127.0.0.1:8000/(  on login ofter to opne to Dashboard)
        path('', views.dashboard_view,name='dashboard'),

   step -3 login page
    frist  to  register to user then to login  with email and password
    email to   Unique
     to  forms.py to use login page to create

class LoginForm(forms.Form):
    email=forms.EmailField(max_length=200)
    password=forms.CharField(max_length=200)

      path- path('login/', views.login_view,name='login'),
      urls-http://127.0.0.1:8000/login/

   then  login user to go to   Dashboard page to login to show  who to login and to and back to login
   to login page to to logout to logout this page

   def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login")


    using this  code

     step 4
   email - post to save to all post in with user name  to save pic name
   with  Unique  folder to save post


 step 5

 post show to setting.py

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 'data' is my media folder
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'


this setting to use to media to show to post
and url.py + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

to add media root to  aad post
 i completed this tast for your requirements pls check and feedback me

 Thank You
 Name -Neetu Kushwaha
 gmail-neetu.python@gmail.com



