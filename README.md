# django-graphql-playground

[Apollo GraphQL Playground](https://github.com/prisma/graphql-playground) as a Django view

![Screenshot](https://cl.ly/46a5bdd1b6bf/Image%2525202019-01-10%252520at%2525205.32.57%252520PM.png)

#### Install
`$ pip install django-graphql-playground`

#### Configure 

```python
# settings.py

INSTALLED_APPS = [
    ...
    'graphql_playground',
]
```

```python
# urls.py

urlpatterns = [
    ...
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="<your_graphql_endpoint>")),
]
```
You can pass in any valid GraphQL Playground property as an argument to `GraphQLPlaygroundView.as_view`. A full list of supported properties can be found [here](https://github.com/prisma/graphql-playground#properties)

See `example/` for more details.



#### Graphene Django GraphiQL Replacement 

You can replace the GraphiQL in the graphene_django GraphQLView by using the `GrapeheneGraphQLView` instead of `GraphQLView`. The `graphiql` argument will now enable/disable the playground instead of GraphiQL.

```python
# urls.py
from graphql_playground.graphene import GraphenePlaygroundView

urlpatterns = [
    ...
    path('graphql', GraphenePlaygroundView.as_view(graphiql=True)),
]
```