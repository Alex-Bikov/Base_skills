# import functools
# # from collections.abc import Callable
# #
# #
# # def check_permission(user: str) -> Callable:
# #     def func_dec(func: Callable) -> Callable:
# #
# #         @functools.wraps(func)
# #         def wrapper(*args, **kwargs):
# #             if user in user_permissions:
# #                 result = func(*args, **kwargs)
# #                 return result
# #             else:
# #                 raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
# #         return wrapper
# #     return func_dec
# #
# #
# # user_permissions = ['admin']
# #
# #
# # @check_permission('admin')
# # def delete_site():
# #     print('Удаляем сайт')
# #
# #
# # @check_permission('user_1')
# # def add_comment():
# #     print('Добавляем комментарий')
# #
# #
# # delete_site()
# # add_comment()


