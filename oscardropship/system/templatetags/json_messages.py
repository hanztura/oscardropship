import json

from django import template
from django.contrib.messages import get_messages

register = template.Library()


@register.simple_tag
def message_to_json(request):
    storage = get_messages(request)
    messages = []
    for message in storage:
        messages.append({
            'message': str(message),
            'tags': message.tags,
            'level': message.level
        })
    return json.dumps(messages)
