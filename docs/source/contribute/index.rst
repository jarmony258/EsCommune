**********
Contribute
**********

🗺 文档仓库 `GitHub <https://github.com/Alex-gift-hit/EsCommune>`_

.. contents:: Table of Contents

创建一个虚拟环境，```python>=3.12```。

.. code-block:: console

    conda create -y -n escommune python=3.12

虚拟环境中做下列安装。

.. code-block:: console

    cd EsCommune
    pip install .

之后 :guilabel:`build` 就可以在本地浏览器查看效果，与官网一致。

sphinx
======

Build
-----

.. code-block:: console

   (.venv) $ sphinx-build -M html docs/source/ build/

:Documentation:
    https://www.sphinx-doc.org/en/master/

sphinx-rtd-theme
================

:Documentation:
    https://sphinx-rtd-theme.readthedocs.io/.

Emoji
=====

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