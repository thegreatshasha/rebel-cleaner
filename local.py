''' Local settings for whitelabel sites. Here you can add tokens specific to your
    development instance and any other overrides needed to support development. '''
from django.conf import settings
from engine.settings import ENGINE_CONSUMER_KEYS, ENGINE_SETTINGS


REBELMOUSELABS_DOMAIN = '{}.rebelmouselabs.com'.format(settings.DEV_INST_NAME)

ENGINE_SETTINGS['rebelmouse']['site_id'] = 0
#uncoment it if you want to pretend the Disney
#ENGINE_SETTINGS['disneycitizenkid']['domains'].append(REBELMOUSELABS_DOMAIN)
#ENGINE_SETTINGS['disneycitizenkid']['site_id'] = 1

#uncoment it if you want to pretend the Dodo
# Use *.rebelmouselab.com domain for thedodo.com site by default
#ENGINE_SETTINGS['dodo']['domains'].append(REBELMOUSELABS_DOMAIN)
#ENGINE_SETTINGS['disneycitizenkid']['site_id'] = 1

#uncoment it if you want to pretend the collective.mtv.com
ENGINE_SETTINGS['mtvcollective']['domains'].append(REBELMOUSELABS_DOMAIN)
# the main site
ENGINE_SETTINGS['mtvcollective']['site_id'] = 1
# mtv show site id like teen wolf
ENGINE_SETTINGS['teenwolf']['site_id'] = 2

#uncoment it if you want to pretend the IntelAmazon
#ENGINE_SETTINGS['intelamazon']['site_id'] = 1

ENGINE_CONSUMER_KEYS['rebelmouse'] = {
    'twitter': (
        'GwRKDhH9sMHfYqvd3zkoitQaN',
        'xYAVHXexyZvv4WOw5QEUke8I6aWbkruylDIXzgTgVCkBKa7U80',
    ),
    'facebook': (
        '',
        '',
    ),
    'google': (
        '',
        '',
    ),
    'google_ios': (
        '',
        '',
    ),
    'instagram': (
        '',
        '',
    ),
    'flickr': (
        '',
        '',
    ),
    'foursquare': (
        '',
        '',
    ),
    'stocktwits': (
        '',
        '',
    ),
    'mailchimp': (
        '',
        '',
    ),
    'linkedin': (
        '',
        '',
    ),
}

ENGINE_CONSUMER_KEYS['dodo'] = ENGINE_CONSUMER_KEYS['nytimes'] = ENGINE_CONSUMER_KEYS['teenwolf'] = ENGINE_CONSUMER_KEYS['mtvcollective'] = ENGINE_CONSUMER_KEYS['rebelmouse']
ENGINE_SETTINGS['dodo']['site_id'] = 2
ENGINE_SETTINGS['dodo']['site_id'] = 1
