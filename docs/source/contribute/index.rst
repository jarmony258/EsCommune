**********
Contribute
**********

🗺 文档仓库 `GitHub <https://github.com/Alex-gift-hit/EsCommune>`_ 任何问题可以提Issue。

.. code-block:: console

    git clone https://github.com/Alex-gift-hit/EsCommune.git
    cd EsCommune


创建一个虚拟环境，```python>=3.12```。

.. code-block:: console

    conda create -y -n escommune python=3.12
    conda activate escommune

虚拟环境中做下列安装。

.. code-block:: console

    pip install .



之后 :guilabel:`build` 就可以在本地浏览器查看效果，与官网一致。

.. code-block:: console

    sphinx-build -M html docs/source/ build/

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