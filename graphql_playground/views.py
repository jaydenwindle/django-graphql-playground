import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import TemplateView


class GraphQLPlaygroundView(TemplateView):
    template_name = "playground/playground.html"

    endpoint = None
    subscription_endpoint=None
    workspace_name=None
    config=None
    settings=None

    def __init__(self,
                 endpoint=None,
                 subscription_endpoint=None,
                 workspace_name=None,
                 config=None,
                 settings=None,
                 **kwargs):
        super(GraphQLPlaygroundView, self).__init__(**kwargs)
        self.options = {
            'endpoint': endpoint,
            'subscriptionEndpoint': subscription_endpoint,
            'workspaceName': workspace_name,
            'config': config,
            'settings': settings,
        }

    def get_context_data(self, *args, **kwargs):
        context = super(GraphQLPlaygroundView, self).get_context_data(*args, **kwargs)
        context['options'] = json.dumps(self.options, cls=DjangoJSONEncoder)
        return context
