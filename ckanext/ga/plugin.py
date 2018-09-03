import os

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def get_ga_id():
    return os.environ['GA_ID']


class GaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ga')

    def get_helpers(self):
        return {'get_ga_id': get_ga_id}
