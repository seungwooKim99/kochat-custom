"""
@auther Hyunwoong
@since 7/1/2020
@see https://github.com/gusdnd852
"""

from kocrawl.dust import DustCrawler
from kocrawl.weather import WeatherCrawler
from kochat.app import Scenario
from kocrawl.map import MapCrawler

# test code
from api.edu import EduAnswerer

edu = Scenario(
    intent='edu',
    api=EduAnswerer().request,
    scenario={
        'KEYWORD': [],
    }
)