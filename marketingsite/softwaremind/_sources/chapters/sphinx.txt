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

A sphinx theme is, at bottom, a simple thing.
A directory in the `docs/` folder, named 'mytheme', containing
`styles/style.css` and a `theme.conf` file.

Creating one from scratch is possible, but a far far simpler approach is
to copy the `bizstyle` directory found in `/usr/local/lib/python3.6/dist-packages/sphinx/themes/bizstyle` into our docs dir, then rename to 'mytheme'

At this point alter the css as below

Now we can start making changes as we want and grow our style.


Lets build the simplest possible Sphinx theme in the simplest possible
way.

::
   #go to the docs dir for the sphinx project
   cd docs/
   mkdir -p themes/darktheme/static
   touch themes/darktheme/theme.conf
   touch themes/darktheme/static/style.css

   in `conf.py` alter
   #the theme name (based on dir)
   html_theme = 'darktheme'
   #where to find the subdir
   html_theme_path = ['themes']

   in `theme.conf`
   [theme]
   inherit = alabaster
   stylesheet = style.css
   pygments_style = pygments.css

   in style.css
   body { color:red; }

Now we *should* have the alabaster style but with red text.
Cool.




We might want to build our own custom theme. In fact this is a lot of
fun.  So the best way is to steal an existing theme, lets say
alabaster, and add to our docs directory in _template

Lets say we copy the directory::
  
  ~/venvs/book/lib64/python3.6/site-packages/alabaster/
  /usr/local/lib/python3.6/dist-packages/alabaster

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




Adjusting the templates.
------------------------

Let's just make a quick change to layout.html in `mytheme`, by say adding
"Helloworld" to the footer, re run it and - yes we have a working theme.

Now we want to find the `basic` theme - that everything else derives from.
This is in the site-packages/sphinx/themes/basic directory.

I want to add a nice "next page" link to my docs, to keep the flow of the book
working.  There is a hint in alabaster::

  {# Disable base theme's top+bottom related navs; we have our own in sidebar #}
  {%- block relbar1 %}{% endblock %}
  {%- block relbar2 %}{% endblock %}

So what is relbar1 and 2? Lets see if we can find them in `basic`
templates.  Yes, in basic/layout.html, there is a relbar `macro` (yes
Jinja2 has macros, which are just functions), and that is called in 2
locations relbar1 and 2.

  {%- block relbar1 %}{{ relbar() }}{% endblock %}

So I am going to steal that macro, and use it in my template,
and adjust it to look right

Progress on this - look for nextprev macro
We can use access keys as well to flip through pages 

Customisation
-------------

If we look at a template, we can see a lot of Jinja2 template
variables, such as `{{ theme_font_size }}`. These are derived from the
theme.conf settings, where the prefix `theme_` is appended to each
variable in the conf (.ini style)

These varables are then pushed into the jinja tempaltes of sphinx and
globally accessible.

We can show this by just adding `{{ theme_font_size }}` to one of our
tempaltes and we will see '17px'.  Thats how all our conf.py changes
are available.

Making changes to theme options.
So all the theme options in `theme.conf`, are then passed into templates
as theme_ prefix.

You can change the settings using ::

 html_theme_options = {'nosidebar' : True,
                      'show_related' : True,
                      'font_size': '32px', <<<<<<<<<<<<< theme_font_size
 }

Biblio
------

http://sphinxcontrib-napoleon.readthedocs.org/en/latest/

http://pythonhosted.org/sphinxjp.themes.basicstrap/

http://blog.jetstrap.com/2013/07/less-like-bootstrap/

The dirt simple sphinx approach for all python projects
=======================================================

Autogenerate a API page.
Use source link on
Then refer to the modules like raw::

   :py:mod:`mikado.config'

   which will link to the api and source.
   So we have a simple, easy way to write prose docs and
   still have all that autogenerated goodness.

   The details are in the docstrings in the module, but the *context*
   is prose in the front end.  SImple and looks good.

   How to do the logo thing...
   

--------
Headings
--------

::
  There is a sensible order here - the "thickest" character is hight (# is thicker than = than -)
  And the higher headings are double underlined, then single underlined

  #########
  Heading 0
  #########
  Heading 0 is for Book titles and so forth
  Do not use unless writing very high level TOCs

  =========
  Heading 1
  =========
  Heading 1 is to be the title page for a single doc / module

  ---------
  Heading 2
  ---------

  Heading 3
  =========

  Heading 4
  ---------

  Heading 5
  ~~~~~~~~~
