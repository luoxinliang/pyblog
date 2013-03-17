import template
from django.conf import settings
from django.http import HttpResponse
from django.template.base import TemplateDoesNotExist

def render_string(template_name, **kwargs):
    """Generate the given template with the given arguments.

    We return the generated string. To generate and write a template
    as a response, use render() above.
    """
    template_path = settings.TEMPLATE_DIRS[0]
    if template_path:
        loader = template.Loader(template_path)
        try:
            t = loader.load(template_name)
        except:
            raise
        return t.generate(**kwargs)
    else:
        error_msg = "TEMPLATE_DIRS is not set in settings"
        raise TemplateDoesNotExist(error_msg)

def render_response(template_name, **kwargs):
    httpresponse_kwargs = {'mimetype': kwargs.pop('mimetype', None)}
    return HttpResponse(render_string(template_name, **kwargs), **httpresponse_kwargs)

