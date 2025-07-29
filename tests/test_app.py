import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from app.models import Job

class JobAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    @patch('app.routes.job_repository')
    def test_create_job(self, mock_repo):
        mock_job = Job(id='60d5ec49e03e4e28c3c3e4f5', title='Software Engineer', description='Develop amazing things.', budget=120000, country='USA')
        mock_repo.create.return_value = mock_job

        response = self.client.post('/jobs/', json={
            'title': 'Software Engineer',
            'description': 'Develop amazing things.',
            'budget': 120000,
            'country': 'USA'
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Software Engineer', response.data)

    @patch('app.routes.job_repository')
    def test_get_jobs(self, mock_repo):
        mock_jobs = [
            Job(id='60d5ec49e03e4e28c3c3e4f5', title='Software Engineer', description='Develop amazing things.', budget=120000, country='USA'),
            Job(id='60d5ec49e03e4e28c3c3e4f6', title='Product Manager', description='Manage amazing products.', budget=110000, country='Canada')
        ]
        mock_repo.get_all.return_value = mock_jobs

        response = self.client.get('/jobs/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Software Engineer', response.data)
        self.assertIn(b'Product Manager', response.data)

if __name__ == '__main__':
    unittest.main()
