from setuptools import setup

# because I love me some pypi
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
  name='flask-meta',
  author = "Jason Goldberger",
  author_email = "jason@datamelon.io",
  version='0.1.0a',
  description = ("""This is a flask app for quickly making fully functional
      flask apps. It might become a generator by neccessity. We'll see."""),
  install_requires=required
  #entry_points="""
  #  [console_scripts]
  #  flask-meta=appmeta:cli
  #"""
)

#A note:
#run `pip install --editable .` in terminal to install as dev

