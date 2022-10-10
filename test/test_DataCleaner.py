import json
from unittest import TestCase

from service.DataCleaner import DataCleaner
from service.Persistence.PersistenceManager import PersistenceManager


class TestDataCleaner(TestCase):

    def test_clean_data(self):
        dirty = [
            {
                'tags_mbits': 'test/holi,test/mola'
            }
        ]
        clean = [
            {
                'tagsAmbits': ['holi', 'mola']
            }
        ]
        cleaned = DataCleaner.clean_data(dirty)
        self.assertListEqual(cleaned, clean, "error")

    def test_treat_tags(self):
        dirty = 'test/holi,test/mola'
        clean = ['holi', 'mola']
        cleaned = DataCleaner.treat_tags(dirty)
        self.assertListEqual(cleaned, clean, "error")

    def test_filter_data_by_normal(self):
        new_data = [
            {
                'codi': 1234,
                'denominacio': 'ous ferrats'
            },
            {
                'codi': 5678,
                'denominacio': 'ous dusos'
            },
            {
                'codi': 9012,
                'denominacio': 'ous estrellats'
            }
        ]

        old_data = [
            {
                'codi': 1234,
                'denominacio': 'ous ferrats'
            },
            {
                'codi': 5678,
                'denominacio': 'ous dusos'
            }
        ]
        filtered_data = DataCleaner.filter_data_by(new_data, old_data, [])
        self.assertListEqual(filtered_data, [{'codi': 9012, 'denominacio': 'ous estrellats'}])

    def test_filter_data_by_diff_keys(self):
        new_data = [
            {
                'codi': 1234,
                'denominacio': 'ous ferrats'
            },
            {
                'codi': 5678,
                'denominacio': 'ous durs'
            },
            {
                'codi': 9012,
                'denominacio': 'ous estrellats'
            }
        ]

        old_data = [
            {
                'codi': 1234,
                'denominacio': 'ous ferrats'
            },
            {
                'codi': 5678,
                'denominacio': 'ous dusos'
            }
        ]
        filtered_data = DataCleaner.filter_data_by(new_data, old_data, [])
        expected = [
            {'codi': 5678, 'denominacio': 'ous durs'},
            {'codi': 9012, 'denominacio': 'ous estrellats'}

        ]
        self.assertListEqual(filtered_data, expected)

    def test_filter_data_by_new_less(self):
        new_data = [
            {
                'codi': 1234,
                'denominacio': 'ous ferrats'
            },
            {
                'codi': 5678,
                'denominacio': 'ous dusos'
            },
            {
                'codi': 9012,
                'denominacio': 'ous estrellats'
            }
        ]

        old_data = [
            {
                'codi': 1234,
                'denominacio': 'ous ferrats'
            },
            {
                'codi': 5678,
                'denominacio': 'ous dusos'
            },
            {
                'codi': 9321,
                'denominacio': 'ous passats aigua'
            },
            {
                'codi': 5432,
                'denominacio': 'ous secs'
            }
        ]
        filtered_data = DataCleaner.filter_data_by(new_data, old_data, [])
        expected = [
            {'codi': 9012, 'denominacio': 'ous estrellats'}

        ]
        self.assertListEqual(filtered_data, expected)