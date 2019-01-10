# django-graphql-playground

[Apollo GraphQL Playground](https://github.com/prisma/graphql-playground) as a Django view

![Screenshot](https://cl.ly/46a5bdd1b6bf/Image%2525202019-01-10%252520at%2525205.32.57%252520PM.png)

#### Install
`$ pip install django-graphql-playground`

#### Configure 
```python
# urls.py

urlpatterns = [
    ...
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="<your_graphql_endpoint>")),
]
```
See `example/` for more details.
