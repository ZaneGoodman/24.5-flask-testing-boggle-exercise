from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        with self.client:
            resp = self.client.get('/')
            html = resp.get_data(as_text=True)
            self.assertIn("board", session)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button id="btn">Submit guess!</button>', html)
            self.assertIsNone(session.get('highscore'))

    def test_if_valid_word(self):
        with self.client as client:
            with client.session_transaction() as session:
                session["board"] = [["H", "A", "P", "P", "Y"],
                                    ["H", "A", "P", "P", "Y"],
                                    ["H", "A", "P", "P", "Y"],
                                    ["H", "A", "P", "P", "Y"],
                                    ["H", "A", "P", "P", "Y"]]
            resp = self.client.get('/check-word?word=happy')
            self.assertEqual(resp.json["result"], 'ok')

    def test_if_not_valid_word(self):
        with self.client:
            self.client.get('/')
            resp = self.client.get('/check-word?word=difficult')
            self.assertEqual(resp.json['result'], 'not-on-board')

    def test_if_non_english_word(self):
        with self.client:
            self.client.get('/')
            resp = self.client.get('/check-word?word=jkl;asdslnkhklgsdlh')
            self.assertEqual(resp.json['result'], 'not-word')
