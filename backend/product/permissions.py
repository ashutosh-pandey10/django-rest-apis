from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    '''
    3.
    '''
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    '''
    4.
        Below code will not work with "perms_map". Why?
        Becasue the class doesnot recognise it as a Admin user
        
        In order to specify that, we will pass as filter where this
        permission is called in the view class.
    '''
    """
    2.
    """
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return True
    #     return super().has_permission(request, view)

        
    '''
    1. 
        This is a working model of how the different permissions can
        be assigned to different users
    '''
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    '''
        ".is_staff" flag : 
    
    '''
    #     if user.is_staff: 
    #         if user.has_perm("product.create_product"): # In the argument, its
    #                                                     # AppName.action_modelName
    #             return True
    #         if user.has_perm("product.view_product"):
    #             return True
    #         if user.has_perm("product.change_product"):
    #             return True
    #         if user.has_perm("product.delete_product"):
    #             return True
    #         return False
        
    #     return False