import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.fields import DjangoConnectionField
from .models import Branch, Bank

# Relay Node for Bank
class BankNode(DjangoObjectType):
    """
    GraphQL Node for Bank model.
    Implements Relay interface for connection support.
    """
    class Meta:
        model = Bank
        interfaces = (relay.Node,)
        fields = '__all__'  # include all fields

# Relay Node for Branch
class BranchNode(DjangoObjectType):
    """
    GraphQL Node for Branch model.
    Includes bank as nested object.
    """
    class Meta:
        model = Branch
        interfaces = (relay.Node,)
        fields = '__all__'

# GraphQL Query
class Query(graphene.ObjectType):
    """
    Root GraphQL query.
    Provides Relay-style connections for branches and banks.
    """
    branches = DjangoConnectionField(BranchNode)
    banks = DjangoConnectionField(BankNode)

# Create schema object
schema = graphene.Schema(query=Query)
