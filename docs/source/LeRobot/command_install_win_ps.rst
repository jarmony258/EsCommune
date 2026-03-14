*********************************
Install LeRobot on Linux/Windows
*********************************

💌 B站官方 `Python现代包架构 LeRobot环境配置与安装(win) <https://www.bilibili.com/video/BV1rWSyBEEBr/>`_

前置需求
=================
conda python的虚拟环境是必须的。

Linux
-----

Miniforge(conda环境)

.. code-block:: console

    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

.. code-block:: console

    bash Miniforge3-$(uname)-$(uname -m).sh

如果是新的ubuntu系统，为了能 install lerobot。还需要一些额外的系统依赖。

.. code-block:: console

    sudo apt update

.. code-block:: console

    sudo apt-get install cmake build-essential python3-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev

Windows
-------

安装anaconda(conda环境)，git即可。

https://git-scm.com/

https://www.anaconda.com/

Environment Setup
=================

.. code-block:: console

    conda create -y -n lerobot python=3.12

.. code-block:: console

    conda activate lerobot

激活lerobot环境。之后所有的pip安装，都会在这个环境里。需要注意的是conda-forge ffmpeg并不是python pkg，所以并不会出现在`pip list`里，需要使用`conda list`.

.. code-block:: console

    conda install ffmpeg=7.1.1 -c conda-forge

.. note::

    Windows安装ffmpeg可能会使虚拟环境受到破坏，如果出现问题，例如无法使用pip. 可以试着更低的版本。

    .. code-block:: console

	    conda install ffmpeg=7.1.0 -c conda-forge --no-deps


		

CMD中使用where命令查看具体的位置。PowerShell中使用where.exe命令查看具体位置。

.. code-block:: console

    (lerobot) F:\Git-Hub\lerobot>where ffmpeg
    G:\ProgramFile\Anaconda2506\envs\lerobot\Library\bin\ffmpeg.exe


Install LeRobot
===============

强烈建议从源码处安装lerobot,可以自己改代码。

毕竟是开源项目，里面很多bug，有时候自己发现了就可以改，例如windows下的openCV backend选择问题。

.. code-block::

    git clone https://github.com/huggingface/lerobot.git
    cd lerobot

    # 编辑模式下安装
    pip install -e .


.. note::

    编辑模式下安装的是默认依赖，可选依赖不会安装，例如 feetech-servo-sdk.


Install Motor Optional dependencies
======================================

.. code-block::

    pip install -e ".[feetech]" # or "[dynamixel]" for example



Ref
======

.. [1] https://huggingface.co/docs/lerobot/installation

.. [2] https://github.com/TheRobotStudio/SO-ARM100