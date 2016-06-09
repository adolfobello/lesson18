from .base import *

## Los valores de los siguientes archivos (si existen)
## sobre-escribiran los valores de base.py.
## Todos los archivos pueden existir o no pero solo uno de ellos
## tendra los settings; los demas vacios.
## Hay que reiniciar el server (runserver)

try:
    from .local import *
except:
    pass


try:
    from .production import *
except:
    pass


try:
    from .any_environment_you_might_have import *
except:
    pass
