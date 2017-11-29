====================================
Documenting Your project with Sphinx
====================================

Documentation matters.

And documentation that visually helps people find their way through
the data, affords people the navigation they need, will help poor overworked
slobs like you and I get to the info we need quicker and less stressed.

So I am reviewing a whole slew of areas

* generating documents from source code
* API and narrative documentation
* Testing the docs and doctests
* customising the look and feel
  - bootstrap
  - styleguides
* Traditional place to start for OSS contributions


Customising Projects all the way
--------------------------------



Custom Themes
-------------

We might want to build our own custom theme. In fact this is a lot of
fun.  So the best way is to steal an existing theme, lets say
alabaster, and add to our docs directory in _template

Lets say we copy the directory::
  
  ~/venvs/book/lib64/python3.6/site-packages/alabaster/

to::

  ~/projects/mytheme

Then::

  ln -s ~/projects/mybook/docs/_templates/mytheme ~/projects/mytheme
  
We then need to visit the sphinx project, and adjust the conf.py file
as::

  html_theme = 'mytheme'
  html_theme_path = ['_templates/']

Note the the theme path is to the *root* of the theme directories.
And note that we have a symlink to the theme path in our project.

We can later on, turn our theme into a python package and install via
pip - just like alabaster was, and it will be available as a name in
the `html_theme`.



  

Biblio
------

http://sphinxcontrib-napoleon.readthedocs.org/en/latest/

http://pythonhosted.org/sphinxjp.themes.basicstrap/

http://blog.jetstrap.com/2013/07/less-like-bootstrap/
