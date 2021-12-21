from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class AdminRequiredMixins():
    def dispatch(self, request, *args, **kwars):
        if not request.user.es_administrador:
            raise PermissionDenied
        return super(AdminRequiredMixins, self).dispatch(request, *args, **kwars)


class PermisosMixins(object):
    def dispatch(self, request, *args, **kwars):
        if request.user.es_escritor:
            return super().dispatch(request, *args, **kwars)
        return redirect("ingresar")
