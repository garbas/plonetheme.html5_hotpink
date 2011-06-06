====================
HTML5 Hot Pink Theme
====================

Installable theme for `Plone`_ (using `plone.app.theming`_).

:Source: https://github.com/garbas/plonetheme.html5_hotpink
:Issues: https://github.com/garbas/plonetheme.html5_hotpink/issues
:Original theme: http://jayj.dk/2011/html5-theme-v2
:Licence: http://www.opensource.org/licenses/bsd-license.php

Since original theme is named ``HTML5``, which is a little to too common name,
I renamed it to ``HTML5 Hot Pink``.


.. contents::


Installation
============

Using buildout
--------------

Add ``plonetheme.html5_hotpink`` to eggs section of your zope client.::
    [instance]
    ...
    eggs =
        ...
        plonetheme.html5_hotpink


Using .zip
----------

::

    % git clone git://github.com/garbas/plonetheme.html5_hotpink.git
    % cd plonetheme.html5_hotpink
    % git archive --format=zip --prefix=html5_hotpink/ HEAD:plonetheme/html5_hotpink/static/ > html5_hotpink.zip

Import created zip file via ``@@theming-controlpanel`` -> ``Import theme`` tab.


Activating theme
----------------

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable
theme`` check box and select ``HTML5 Hot Pink (plonetheme.html5_hotpink)`` from
dropdown.

Parameters
==========

    * ``site-title``, Default: ``string: A HTML5 Hot Pink Theme``

        Site title. 

    * ``site-description``, Default: ``string: This is an awesome HTML5 Hot Pink theme!``

        Site description.

    * ``footer``, Default: ``string: Copyright &copy; 2011 ...``

        Footer of site. HTML marks allowed.

    * ``notheme``, Default: ``python: 'ajax_load' in request.form``

        Expression which makes page unthemed.


Credits
=======

    * `Rok Garbas`_, initial implementation
    * `Jesper`_, original theme author


Changelog
=========

0.1 - 2011-06-05
----------------

    * initial implementation of theme with Diazo_ rules.
      [garbas]


.. _`Rok Garbas`: http://www.garbas.si
.. _`Jesper`: http://jayj.dk

.. _`Plone`: http://plone.org
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Diazo': http://diazo.org
