from app import RandomUser
import unittest
from unittest.mock import patch, Mock

class TestRandomUser(unittest.TestCase):

    @patch('requests.get')
    def test_get_user(self, mock_obj):
        instance = RandomUser()

        mock_obj.return_value.raise_for_status.return_value = None
        mock_obj.return_value.json.return_value = {
            'results': [{
                'gender': 'male', 
                'name': {
                    'first': 'Hawx',
                    'last': 'OverKill'
                }, 
                'location': {
                    'city': 'Chennai', 
                    'country': 'India'
                }, 
                'email': 'hawx.overkill@gmail.com'
            }]
        }

        output = instance.get_user()
        
        #test cases
        mock_obj.assert_called_once()
        self.assertEqual(output,{'Name': 'Hawx OverKill', 'Gender': 'male', 'Email': 'hawx.overkill@gmail.com', 'Location': 'Chennai India'})

if __name__ == '__main__':
    unittest.main()