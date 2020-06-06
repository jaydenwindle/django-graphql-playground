from graphene_django.views import GraphQLView as _GraphQLView
from .views import GraphQLPlaygroundView as _PlaygroundView



class GraphenePlaygroundView(_GraphQLView):
    """ This is a wrapper around :mod:`graphene_django`'s :class:`GraphQLView` that replaces `graphiql` with `graphql-playground`.

    Accepts the same parameters as `GraphQLPlaygroundView`, all others are passed to `GraphQLView`.
    """
    def __init__(self, 
                endpoint=None,
                subscription_endpoint=None,
                workspace_name=None,
                config=None,
                settings=None,
                *args, **kwargs):

        kwargs['graphiql'] = True
        super().__init__(*args, **kwargs)
        self.playground_view = _PlaygroundView.as_view(
                 endpoint=endpoint,
                 subscription_endpoint=subscription_endpoint,
                 workspace_name=workspace_name,
                 config=config,
                 settings=settings)

    def render_graphiql(self, request, **data):
        return self.playground_view(request)
