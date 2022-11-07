import json
from unittest import TestCase

from service.DataCleaner import DataCleaner
from service.Persistence.PersistenceManager import PersistenceManager


class TestDataCleaner(TestCase):

    def test_clean_naming(self):
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
        cleaned = DataCleaner.clean_naming_and_formatting(dirty)
        self.assertListEqual(cleaned, clean, "error")

    def test_clean_data_location(self):
        dirty = [
            {
                'tags_mbits': 'test/holi,test/mola',
                'comarca_i_municipi': 'agenda:ubicacions/barcelona/anoia/capellades'
            }
        ]
        clean = [
            {
                'tagsAmbits': ['holi', 'mola'],
                'comarcaIMunicipi': 'Capellades, Anoia, Barcelona'

            }
        ]
        cleaned = DataCleaner.clean_naming_and_formatting(dirty)
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
        filtered_data = DataCleaner.filter_data_by(new_data, old_data, ['codi'])
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
        filtered_data = DataCleaner.filter_data_by(new_data, old_data, ['codi', 'denominacio'])
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
        filtered_data = DataCleaner.filter_data_by(new_data, old_data, ['codi'])
        expected = [
            {'codi': 9012, 'denominacio': 'ous estrellats'}

        ]
        self.assertListEqual(filtered_data, expected)

    def test_clean_location(self):
        dirty = 'agenda:ubicacions/barcelona/anoia/capellades'
        clean = 'Capellades, Anoia, Barcelona'
        res = DataCleaner.clean_location(dirty)
        self.assertEqual(res, clean)

    def test_clean_location_withspaces(self):
        dirty = 'agenda:ubicacions/lleida/segarra/els-plans-de-sio'
        clean = 'Els Plans De Sio, Segarra, Lleida'
        res = DataCleaner.clean_location(dirty)
        self.assertEqual(res, clean)

    def test_merge_geo_information_comarca(self):
        dirty = {
            'comarcaIMunicipi': 'Els Plans De Sio, Segarra, Lleida',
            'localitat': 'Concabella',
        }
        clean = {
            'ubicacio': 'Concabella (Els Plans De Sio, Segarra, Lleida)'
        }
        res = DataCleaner.merge_geoinformation(dirty)
        self.assertDictEqual(res, clean)

    def test_merge_geo_information_regio(self):
        dirty = {
            'regioOPais': 'Comarques barcelonines',
            'localitat': 'Diferents municipis'
        }
        clean = {
            'ubicacio': 'Diferents municipis (Comarques barcelonines)'
        }
        res = DataCleaner.merge_geoinformation(dirty)
        self.assertDictEqual(res, clean)

    def test_merge_geo_information_just_localitat(self):
        dirty = {
            'localitat': 'Barcelona'
        }
        clean = {
            'ubicacio': 'Barcelona'
        }
        res = DataCleaner.merge_geoinformation(dirty)
        self.assertDictEqual(res, clean)

    def test_merge_geo_information_online(self):
        dirty = {

        }
        clean = {
            'ubicacio': 'Activitat online'
        }
        res = DataCleaner.merge_geoinformation(dirty)
        self.assertDictEqual(res, clean)

    def test_extract_remaining_information(self):
        dirty = {
            "adreca": "C. Macarnau, 55",
            "comarcaIMunicipi": "agenda:ubicacions/girona/garrotxa/olot",
            "espai": "Espai Cr\u00e0ter"
        }
        expected_res = {
            "adreca": "C. Macarnau, 55",
            "espai": "Espai Cr\u00e0ter"
        }
        expected_rem = {
            "comarcaIMunicipi": "agenda:ubicacions/girona/garrotxa/olot"
        }
        res, rem = DataCleaner.extract_remaining_information(dirty, ['comarcaIMunicipi'])
        self.assertDictEqual(expected_res, res)
        self.assertDictEqual(expected_rem, rem)

    def test_merge_geo_information_extra_info(self):
        dirty = {
            'regioOPais': 'Comarques barcelonines',
            'localitat': 'Diferents municipis',
            "adreca": "C. Macarnau, 55"
        }
        clean = {
            "adreca": "C. Macarnau, 55",
            'ubicacio': 'Diferents municipis (Comarques barcelonines)'

        }
        res = DataCleaner.merge_geoinformation(dirty)
        self.assertDictEqual(res, clean)


