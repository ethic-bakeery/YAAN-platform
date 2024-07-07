from rest_framework import serializers
from .models import User, Profile, Poll, Question, Choice, Feedback, Post, Event, ChatMessage, LiveChatSession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'state', 'phone_number', 'date_of_birth', 'local_government', 'is_volunteer']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_picture']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'poll', 'text', 'choices']

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'updated_at', 'image', 'questions']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'poll', 'user', 'comment']

class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)
    dislikes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'created_by', 'created_at', 'updated_at', 'likes', 'dislikes']

class EventSerializer(serializers.ModelSerializer):
    attendees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'updated_at', 'start_time', 'end_time', 'location', 'attendees']
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'recipient', 'message', 'timestamp']

class LiveChatSessionSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = LiveChatSession
        fields = ['id', 'participants', 'created_at', 'updated_at']
