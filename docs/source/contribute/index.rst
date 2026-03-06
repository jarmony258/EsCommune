**********
Contribute
**********

🗺 文档仓库 `GitHub <https://github.com/Alex-gift-hit/EsCommune>`_

.. contents:: Table of Contents

创建一个虚拟环境，```python>=3.10```。

虚拟环境中做下列安装。之后 :guilabel:`build` 就可以在本地浏览器查看效果，与官网一致。

sphinx
======

Installation
------------

.. code-block:: console

   $ pip install -U sphinx

Build
-----

.. code-block:: console

   (.venv) $ sphinx-build -M html docs/source/ build/

:Documentation:
    https://www.sphinx-doc.org/en/master/

sphinx-rtd-theme
================

Installation
------------

.. code-block:: console

      $ pip install sphinx-rtd-theme

:Documentation:
    https://sphinx-rtd-theme.readthedocs.io/.

Emoji
=====

Installation
------------

.. code-block:: console

   pip install sphinxemoji


Configuration
-------------

.. code-block:: python

   # conf.py
   extensions = [
       '...',
       'sphinxemoji.sphinxemoji',
   ]


:Documentation:
   https://sphinxemojicodes.readthedocs.io/en/stable/


Format
=========

.. code-block:: console

    **********
    Page start
    **********

    head1
    =====

    head2
    -----