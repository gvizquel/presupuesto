# main.py

# Django Libraries
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Thirdparty Libraries
from dal import autocomplete

# Local Folders Libraries
from ..models import Dpt

# from flock.models import Flock


# ========================================================================== #
class MainListView(ListView):
    template_name = 'main/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['add_url'] = '{}:create'.format(object_name)
        context['update_url'] = '{}:update'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        context['title'] = '{}'.format(verbose_name)
        context['breadcrumbs'] = [
            {
                'url': '',
                'name': object_name
            }
        ]
        return context

    class Meta:
        abstract = True


# ========================================================================== #
class MainDetailView(DetailView):
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['title'] = '{} {}'.format(verbose_name, _("Detail"))
        context['breadcrumbs'] = [{
            'url': '{}:list'.format(object_name),
            'name': '{}'.format(verbose_name)
        }]
        context['list_url'] = '{}:list'.format(object_name)
        context['update_url'] = '{}:update'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        return context

    class Meta:
        abstract = True


# ========================================================================== #
class MainCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['title'] = '{} {}'.format(_("Add"), verbose_name)
        context['list_url'] = '{}:list'.format(object_name)
        context['update_url'] = '{}:update'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['breadcrumbs'] = [
            {
                'url': reverse_lazy('{}:list'.format(object_name)),
                'name': '{}'.format(verbose_name)
            },
            {
                'url': '',
                'name': _('Add')
            }
        ]
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        verbose_name = self.model._meta.verbose_name
        create_object = form.save(commit=False)
        create_object.uc = self.request.user
        create_object.save()
        messages.success(
            self.request,
            _('The %(object)s, was succesfully created') % {
                'object': verbose_name}
        )
        return super().form_valid(form)

    class Meta:
        abstract = True


# ========================================================================== #
class MainUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['title'] = '{}'.format(verbose_name)
        context['list_url'] = '{}:list'.format(object_name)
        context['update_url'] = '{}:update'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['action_url'] = '{}:update'.format(object_name)
        context['breadcrumbs'] = [
            {
                'url': reverse_lazy('{}:list'.format(object_name)),
                'name': '{}'.format(verbose_name)
            },
            {
                'url': '',
                'name': _('Update')
            }
        ]
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        verbose_name = self.model._meta.verbose_name
        update_object = form.save(commit=False)
        update_object.um = self.request.user
        update_object.save()
        messages.success(
            self.request,
            _('The %(object)s, was succesfully updated') % {
                'object': verbose_name}
        )
        return super().form_valid(form)

    class Meta:
        abstract = True


# ========================================================================== #
class MainDeleteView(DeleteView):
    template_name = 'base/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['title'] = _("Delete %(obj_name)s") % {
            "obj_name": verbose_name}
        context['action_url'] = reverse_lazy('{}:delete'.format(object_name),
                                             kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return '{}:list'.format(self.model._meta.object_name)

    def delete(self, request, *args, **kwargs):
        delete_object = self.get_object()
        success_url = reverse_lazy(self.get_success_url())
        delete_object.delete()
        return HttpResponseRedirect(success_url)

    class Meta:
        abstract = True


# ========================================================================== #
class EstadoAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para los estado  del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):
        queryset = Dpt.objects.filter(arbol='root.243')

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ========================================================================== #
class MunicipioAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para los municipios del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):

        estado = self.forwarded.get('estado', None)

        if estado:
            queryset = Dpt.objects.filter(
                arbol__startswith='root.243',
                division__icontains='Municipio',
                division_padre=estado
            )
        else:
            queryset = Dpt.objects.filter(
                arbol__startswith='root.243',
                division__icontains='Municipio'
            )

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ========================================================================== #
class ParroquiaAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para las parroquias del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):

        municipio = self.forwarded.get('municipio', None)

        if municipio:
            queryset = Dpt.objects.filter(
                arbol__startswith='root.243',
                division__icontains='Parroquia',
                division_padre=municipio
            )
        else:
            queryset = Dpt.objects.filter(
                arbol__startswith='root.243',
                division__icontains='Parroquia'
            )

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset
