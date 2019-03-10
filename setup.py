from distutils.core import setup
setup(
  name = 'ITRDegreeDays',         # How you named your package folder (MyLib)
  packages = ['ITRDegreeDays'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'It is an open source library for calculating grade days using the simple sine method',   # Give a short description about your library
  author = 'Mauricio Flores Hernández',                   # Type in your name
  author_email = 'mau1361317@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/devmaufh/ITRDegreeDays',   # Provide either the link to your github or to your website
  download_url = 'https://codeload.github.com/devmaufh/ITRDegreeDays/legacy.tar.gz/0.1',    # I explain this later on
  keywords = ['Degree', 'Days','Sin'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)