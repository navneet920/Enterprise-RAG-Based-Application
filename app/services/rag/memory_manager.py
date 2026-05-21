conversation_memory = []


def save_message(role, content):

    conversation_memory.append({
        "role": role,
        "content": content
    })


def get_conversation():

    return conversation_memory[-10:]