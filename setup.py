from distutils.core import setup
setup(
  name = 'mozilla-cloud-services-logger',
  packages = ['mozilla_cloud_services_logger', 'mozilla_cloud_services_logger.django'],
  version = '1.0.1',
  description = 'Tools for producing a common application logging format defined by Mozilla Cloud Services',
  author = 'Les Orchard',
  author_email = 'lorchard@mozilla.com',
  url = 'https://github.com/mozilla/mozilla-cloud-services-logger',
  download_url = 'https://github.com/mozilla/mozilla-cloud-services-logger/tarball/1.0.1',
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
