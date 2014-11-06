import sae
from demonmirror import wsgi

application = sae.create_wsgi_app(wsgi.application)