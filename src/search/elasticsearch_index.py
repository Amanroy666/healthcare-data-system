"""
Elasticsearch Integration for Patient Search
Fuzzy matching and phonetic search for 500K+ records
"""
from elasticsearch import Elasticsearch
from typing import List, Dict

class PatientSearch:
    def __init__(self, hosts=['localhost:9200']):
        self.es = Elasticsearch(hosts)
        self.index = 'patients'
    
    def create_index(self):
        """Create Elasticsearch index with custom analyzers"""
        mapping = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "phonetic_analyzer": {
                            "tokenizer": "standard",
                            "filter": ["lowercase", "phonetic"]
                        }
                    },
                    "filter": {
                        "phonetic": {
                            "type": "phonetic",
                            "encoder": "metaphone"
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "first_name": {
                        "type": "text",
                        "analyzer": "phonetic_analyzer"
                    },
                    "last_name": {
                        "type": "text",
                        "analyzer": "phonetic_analyzer"
                    },
                    "medical_record_number": {"type": "keyword"},
                    "date_of_birth": {"type": "date"}
                }
            }
        }
        
        self.es.indices.create(index=self.index, body=mapping)
    
    def search_patients(self, query: str, fuzzy: bool = True) -> List[Dict]:
        """Search patients with fuzzy matching"""
        search_query = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["first_name^2", "last_name^2", "medical_record_number"],
                    "fuzziness": "AUTO" if fuzzy else 0
                }
            }
        }
        
        results = self.es.search(index=self.index, body=search_query)
        return [hit['_source'] for hit in results['hits']['hits']]
