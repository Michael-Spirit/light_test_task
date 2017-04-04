# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

from rest_framework.reverse import reverse
from rest_framework import status

from accounts.tests.factories import UserFactory
from data.tests.factories import MessageFactory
from data.models import Message


class TestMessage(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

    def test_get_message(self):
        """
        Test GET Message by id
        """
        msg = MessageFactory()

        url = reverse('data:message-detail', kwargs={'pk': msg.pk})
        response = self.client.get(url)
        self.assertContains(response, msg.text)

    def test_get_all_messages(self):
        """
        Test GET all Messages
        """
        msg1 = MessageFactory()
        msg2 = MessageFactory()

        url = reverse('data:message-list')
        response = self.client.get(url)

        self.assertContains(response, msg1.text)
        self.assertContains(response, msg2.text)

    def test_create_message(self):
        """
        Test POST Message
        """
        message_text = 'texttexttext'

        response = self.client.post(
            reverse('data:message-list'), {'text': message_text})
        self.assertContains(response, message_text, status_code=201)

        message = Message.objects.first()
        self.assertEqual(message.text, message_text)

    def test_update_message(self):
        """
        Test UPDATE Message
        """
        new_msg_text = 'not simple text'

        msg = MessageFactory(text='text')

        response = self.client.patch(
            reverse('data:message-detail', kwargs={'pk': msg.id}),
            {'text': new_msg_text})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        msg = Message.objects.first()
        self.assertEqual(msg.text, new_msg_text)

    def test_delete_message(self):
        """
        Test DELETE Message
        """
        msg = MessageFactory()

        self.assertEqual(Message.objects.count(), 1)

        self.client.delete(
            reverse('data:message-detail', kwargs={'pk': msg.id}))
        self.assertEqual(Message.objects.count(), 0)

    def test_create_comment_answer_to_comment(self):
        """
        Test POST answer comment with comment parent
        """
        msg = MessageFactory(text='text')
        comment_text = 'sup bro'

        url = reverse('data:message-list')
        data = {
            'text': comment_text,
            'parent_id': msg.id
        }

        response = self.client.post(url, data, format='json')
        self.assertContains(response, comment_text, status_code=201)

        self.assertEqual(Message.objects.count(), 2)
