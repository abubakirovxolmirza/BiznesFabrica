from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        # 'role': user.get_role(),
	'role_id': user.role.id if user.role else None,
        'user_id': user.id,
    }
