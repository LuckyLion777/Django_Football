from mezzanine import template
from mezzanine.accounts import get_profile_for_user
from mezzanine.conf import settings

register = template.Library()

@register.filter
def get_avatar_path(user):
    return get_profile_for_user(user).avatar.url
