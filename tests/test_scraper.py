import json
import unittest
from io import StringIO
from unittest.mock import call, patch, Mock, ANY

from scraper import get_data, parse_data, save_to_json, main


class BookScraperTestCase(unittest.TestCase):

    def setUp(self):
        self.content = '<html><head><title>Test Book</title></head></html>'

    @patch('scraper.requests.get')
    def test_get_data(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = self.content
        mock_get.return_value = mock_response

        result = get_data('https://example.com/text-book')

        self.assertIn('<html>', result)
        self.assertIn('<title>Test Book</title>', result)
        mock_get.assert_called_once_with('https://example.com/text-book')

    @patch('scraper.requests.get')
    def test_get_data_bad_request(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(AssertionError):
            get_data('https://example.com/text-book')

    @patch('scraper.BeautifulSoup')
    def test_parse_data(self, mock_bs4):
        mock_soup = Mock()
        mock_soup.title.text = 'Test title'
        mock_soup.select.side_effect = [
            [Mock(text='Author')],
            [Mock(text='Description')],
            [Mock(text='5.0')],
            [Mock(text='Genre 1'), Mock(text='Genre 2')],
            [Mock(text='Number of pages 100')]
        ]
        mock_bs4.return_value = mock_soup

        result = parse_data(self.content)

        mock_soup.select.assert_has_calls(
            [
                call('.ContributorLink__name'),
                call('.Formatted'),
                call('.RatingStatistics__rating'),
                call('.BookPageMetadataSection__genreButton .Button__labelItem'),
                call('.FeaturedDetails'),
            ]
        )
        self.assertEqual(result['title'], 'Test title')
        self.assertEqual(result['author'], 'Author')
        self.assertEqual(result['description'], 'Description')
        self.assertEqual(result['rating'], '5.0')
        self.assertEqual(result['genres'], ['Genre 1', 'Genre 2'])
        self.assertEqual(result['details'], 'Number of pages 100')

    @patch('scraper.json.dump')
    def test_save_to_json(self, mock_json_dump):
        data = {
            'title': 'Title',
            'author': 'Test author',
            'description': 'Description',
            'rating': '5.0',
            'genres': ['Genre 1', 'Genre 2'],
            'details': 'Number of pages 100'
        }
        filename = 'data.json'

        save_to_json(data, filename)

        mock_json_dump.assert_called_once_with(data, ANY, indent=4)

    @patch('scraper.json.dump')
    def test_save_to_json_failed(self, mock_json_dump):
        data = {
            'title': 'Title',
            'author': 'Test author',
            'description': 'Description',
            'rating': '5.0',
            'genres': ['Genre 1', 'Genre 2'],
            'details': 'Number of pages 100'
        }
        filename = 'data.json'
        mock_json_dump.side_effect = json.JSONDecodeError('Error', 'Doc', 1)

        with self.assertRaises(json.JSONDecodeError):
            save_to_json(data, filename)

        mock_json_dump.assert_called_once_with(data, ANY, indent=4)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('scraper.save_to_json')
    @patch('scraper.parse_data')
    @patch('scraper.get_data')
    def test_main_success(
            self,
            mock_get_data,
            mock_parse_data,
            mock_save,
            mock_stdout
    ):
        mock_get_data.return_value = 'Test'
        mock_parse_data.return_value = {
            'title': 'Title',
            'author': 'Test author',
            'description': 'Description',
            'rating': '5.0',
            'genres': ['Genre 1', 'Genre 2'],
            'details': 'Number of pages 100'
        }

        main()

        mock_get_data.assert_called_once_with(
            'https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half_Blood_Prince'
        )
        mock_parse_data.assert_called_once_with('Test')
        mock_save.assert_called_once_with(
            {
                'title': 'Title',
                'author': 'Test author',
                'description': 'Description',
                'rating': '5.0',
                'genres': ['Genre 1', 'Genre 2'],
                'details': 'Number of pages 100'
            },
            'harry_potter_and_the_half_blood_prince.json'
        )
        output = mock_stdout.getvalue()
        self.assertIn('Title', output)


