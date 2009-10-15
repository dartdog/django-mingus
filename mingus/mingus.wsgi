import os
import sys

# activate virtualenv
activate_this = os.path.expanduser("~/webapps/devoswco/oswco-env/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, os.path.expanduser("~/webapps/devoswco/oswco-env/"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mingus.settings'

# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

#old
#sys.path.append('%s/../' % os.path.dirname(__file__))
#os.environ['DJANGO_SETTINGS_MODULE'] = 'django_yaba.settings'
#os.environ['PYTHON_EGG_CACHE'] = "%s/cache" % os.path.dirname(__file__)

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

