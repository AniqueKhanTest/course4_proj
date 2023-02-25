from .client import OmdbClient
from .omdbapi_testing import OMDB_API_KEY

def get_client():
    # Create an instance on an OmdbClient using the API_KEY 
    return OmdbClient(OMDB_API_KEY)