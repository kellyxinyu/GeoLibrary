from GeoLibrary import geocoder
import pytest

def test_missing_arguments():
    with pytest.raises(TypeError):
        geocoder.geocoder_gmap('3737 cogdell st')

def test_full_state():
    assert geocoder.geocoder_gmap('3737 cogdell st', 'houston', 'texas', 
                                  'AIzaSyBqr60VzhSJ7eRx6wAyyWG60WZ8tc-sfII')== [29.7581354, -95.4058313]
    
def test_abbr_state():
    assert geocoder.geocoder_gmap('3737 cogdell st', 'houston', 'tx', 
                                  'AIzaSyBqr60VzhSJ7eRx6wAyyWG60WZ8tc-sfII')== [29.7581354, -95.4058313]
    
def test_distancematrix():
    assert geocoder.distancematrix_gmap(29.492175,-98.439082,29.7003979,-95.4280686, 
                                        'AIzaSyBqr60VzhSJ7eRx6wAyyWG60WZ8tc-sfII' ) == {
                    'drive_time_minutes': 183.18,
                    'distance_miles': 196.2
                }