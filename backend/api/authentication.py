from rest_framework.authentication import TokenAuthentication as BasicAuthentication

class TokenAuthentication(BasicAuthentication):
    keyword = "Bearer"