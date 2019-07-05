from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
from graphene.relay import Node
import graphene

from graphQl.models import User as UserModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel
        interface = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_user = MongoengineConnectionField(User)


schema = graphene.Schema(query=Query, types=[User])
