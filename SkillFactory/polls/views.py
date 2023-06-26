from django.http import HttpResponse
from django.template import loader
from configparser import ConfigParser
from configparser import NoSectionError as configparse_err

def get_db_config(db_option):
 config = ConfigParser()

 config.read('/app/django.conf')
 try:
     result = config.get("database", db_option)
 except configparse_err:
    print ('Cannot get {}. There is no such section or config file is unavailable/does not exist').format(db_option)
    exit ()
 return result

def index(request):
    template = loader.get_template('polls/index.html')
    db_name = "database {0}".format(get_db_config("db_name"))
    context = {
        'db_name': db_name,
    }
    return HttpResponse(template.render(context, request))