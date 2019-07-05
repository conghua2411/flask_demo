import json

import graphene


class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    email = graphene.String()
    number = graphene.String()


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(
                name="qweqwe",
                age=123,
                email="qweqwe@asd.asd",
                number="123123123"
            ),
            User(
                name="zxczxc",
                age=321,
                email="zxczxc@asd.asd",
                number="321321312"
            ),
            User(
                name="asdasdasd",
                age=456,
                email="asdasdasd@asd.asd",
                number="456456456"
            )
        ][:first]


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, name):
        if info.context.get('is_vip'):
            name = name.upper()
        user = User(name=name)
        return CreateUser(user=user)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

# query
result = schema.execute(
    '''
    {
        users(first: 1) {
            name
            age
            email
            number
        }
    }
    '''
)

# mutations
result2 = schema.execute(
    '''
    mutation createUser($username: String) {
        createUser(name: $username) {
            user {
                name
            }
        }
    }
    ''',
    variable_values={'username': 'newnew'},
    context={'is_vip': True}
)

items = dict(result2.data.items())
print(json.dumps(items))
