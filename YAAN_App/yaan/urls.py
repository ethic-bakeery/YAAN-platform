from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserView, ProfileView, PollView, QuestionView, ChoiceView, 
    FeedbackView, PostView, EventView, ChatMessageView, LiveChatView
)

router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'profiles', ProfileView)
router.register(r'polls', PollView)
router.register(r'questions', QuestionView)
router.register(r'choices', ChoiceView)
router.register(r'feedbacks', FeedbackView)
router.register(r'posts', PostView)
router.register(r'events', EventView)
router.register(r'chat-messages', ChatMessageView)
router.register(r'live-chat-sessions', LiveChatView)

urlpatterns = [
    path('', include(router.urls)),
]
