# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import ChatMassages
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from .llm import get_vector, get_rag_promt, get_llm

# @receiver(post_save, sender=ChatMassages)
# def pdf_created(sender, instance, created, **kwargs):
#     if created:

#         vectorstore = get_vector(instance.user.username)
#         prompt = get_rag_promt()
#         model = get_llm(vectorstore, prompt)
#         result = model({"query": instance.massage_content})    

#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f'chat{instance.user.username}',
#             {
#                 "type": "chat_message",
#                 "message": result["result"],
#                 "username": 'Chat Bot',
#                 "room": instance.room.id
#             }
#         )