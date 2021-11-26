import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from user.models import User

from TODO.models import ToDo, Project


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        filter_fields = ['is_active']
        fields = '__all__'
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, user_id=graphene.Int(required=True))
    project_by_id = graphene.Field(ProjectType, project_id=graphene.Int(required=True))
    all_todos = DjangoFilterConnectionField(ToDoType)
    todo = relay.Node.Field(ToDoType)


    def resolve_user_by_id(self, info, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def resolve_all_users(root, info):
        return User.objects.all()


    def resolve_project_by_id(self, info, project_id):
        try:
            return Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
