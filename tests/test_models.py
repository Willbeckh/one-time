import unittest
from app.models import User, Pitch, Comment,Vote


class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='test', email='test@code.dev', about_me='developer avocado')
        
    def test_set_password(self):
        self.new_user.set_password('banana')
        self.assertTrue(self.new_user.password_hash is not None)
        
    def test_check_password(self):
        self.new_user.set_password('banana')
        self.assertTrue(self.new_user.check_password('banana'))
        self.assertFalse(self.new_user.check_password('banana123'))
        
     
class TestPitchModel(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(id=1, title='Test', text='This is a test pitch', categories='test', user_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'Test')
        self.assertEquals(self.new_pitch.text, 'This is a test pitch')
        self.assertEquals(self.new_pitch.categories, 'test')
        self.assertEquals(self.new_pitch.user_id, 1)   
        
class TestCommentModel(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(id=1, comment_text='Test', pitch_id=1, user_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_text, 'Test')
        self.assertEquals(self.new_comment.pitch_id, 1)
        self.assertEquals(self.new_comment.user_id, 1)
 
class TestVoteModel(unittest.TestCase):
    def setUp(self):
        self.new_vote = Vote(id=1, upvote=1, downvote=0, pitch_id=1, user_id=1)

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_vote, Vote))

    # def test_check_instance_variables(self):
    #     self.assertEquals(self.new_vote.upvote, 1)
    #     self.assertEquals(self.new_vote.downvote, 0)
    #     self.assertEquals(self.new_vote.pitch_id, 1)
    #     self.assertEquals(self.new_vote.user_id, 1)
        
               

if __name__ == '__main__':
    unittest.main()
