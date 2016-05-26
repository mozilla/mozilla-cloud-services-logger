from distutils.core import setup
setup(
  name = 'mozilla_cloud_services_logger',
  packages = ['mozilla_cloud_services_logger'], # this must be the same as the name above
  version = '1.0',
  description = 'A random test lib',
  author = 'Les Orchard',
  author_email = 'lorchard@mozilla.com',
  url = 'https://github.com/lmorchard/mozilla_cloud_services_logger', # use the URL to the github repo
  download_url = 'https://github.com/lmorchard/mozilla_cloud_services_logger/tarball/0.1', # I'll explain this in a second
  keywords = ['mozilla', 'logging', 'django'],
  classifiers = [
     'Development Status :: 4 - Beta',
     'Environment :: Console',
     'Intended Audience :: Developers',
     'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
     'Operating System :: OS Independent',
     'Topic :: Software Development :: Libraries :: Python Modules',     
  ],
)
