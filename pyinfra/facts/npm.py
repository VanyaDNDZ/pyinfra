# encoding: utf8

from __future__ import unicode_literals

from pyinfra.api import FactBase

from .util.packaging import parse_packages

NPM_REGEX = r'^[└├]\─\─\s([a-zA-Z0-9\-]+)@([0-9\.]+)$'


class NpmPackages(FactBase):
    '''
    Returns a dict of installed npm packages globally or in a given directory:

    .. code:: python

        'package_name': ['version'],
        ...
    '''

    command = 'npm list -g --depth=0'
    default = dict
    use_default_on_error = True

    def command(self, directory=None):
        if directory:
            return 'cd {0} && npm list -g --depth=0'.format(directory)
        else:
            return 'npm list -g --depth=0'

    def process(self, output):
        return parse_packages(NPM_REGEX, output)
