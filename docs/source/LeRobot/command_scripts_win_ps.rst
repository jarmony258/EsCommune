*******
Scripts
*******

💌 B站官方 `LeRobot 30Kg双摄 组装，标定，双平台遥操作 全面一站式解决 <https://www.bilibili.com/video/BV16rrvBiEWa/>`_

Conda Env
=========

.. code-block:: shell

    conda activate lerobot

Find-port [1]_
=========

插入端口，所有已插入的端口都会被脚本识别。

拔出想要知道端口号的端口，键入enter。

.. code-block:: bash

    lerobot-find-port

linux
-----

.. note::

    ubuntu系统可能会有USB设备的访问权限问题。如果访问被拒绝。可以修改访问权限。

    Means that all the users can read&write&execute to devices.

    .. code-block:: bash

        sudo chmod 777 /dev/ttyACM0 & sudo chmod 777 /dev/ttyACM1

Setup-motors [1]_
============

windows
-------

多个舵机使用串行通讯挂在一条舵机总线上(一条线)。通过不同的ID区分。其中 Gripper 的 ID 为6，依次递减。

.. code-block:: console

    lerobot-setup-motors --robot.type=so101_follower --robot.port=COM3

.. code-block:: console

    lerobot-setup-motors --teleop.type=so101_leader --teleop.port=COM4

linux
-----
.. code-block:: console

    lerobot-setup-motors --robot.type=so101_follower --robot.port=/dev/ttyACM1

.. code-block:: console

    lerobot-setup-motors --teleop.type=so101_leader --teleop.port=/dev/ttyACM0

Calibrate [1]_ [2]_
=========

舵机是绝对值磁编码传感器，掉电后角度不丢失。可以360度旋转 即 0-4095（0-360）。

舵机的中点 2048 需要 与 物理结构对应。所以要标定中点（修改中点偏移量）。

结构件安装后，旋转范围有了物理限制。以标定中点为中心点，设置角度限制。

.. warning::

    **尽量使舵机标定的角度限制与物理限制贴合，否则掉电后对机械臂的操作可能超过标定的范围，会出问题！！！**

windows
-------

.. code-block:: console

    lerobot-calibrate  --robot.type=so101_follower --robot.port=COM3 --robot.id=my_awesome_follower_arm # <- Give the robot a unique name

.. code-block:: console

    lerobot-calibrate  --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=my_awesome_leader_arm # <- Give the robot a unique name

标定后的机械臂数据存储在 ``C:\Users\hp四核\.cache\huggingface\lerobot\calibration`` 。如果我们有两条Follower臂，一条19KG，一条30KG，分别标定后都存储在这个位置。

linux
-----
.. code-block:: console

    lerobot-calibrate  --robot.type=so101_follower --robot.port=/dev/ttyACM1 --robot.id=my_awesome_follower_arm # <- Give the robot a unique name

.. code-block:: console

    lerobot-calibrate  --teleop.type=so101_leader --teleop.port=/dev/ttyACM0 --teleop.id=my_awesome_leader_arm # <- Give the robot a unique name

标定后的机械臂数据存储在 ``/home/escommune/.cache/huggingface/lerobot/calibration`` 。如果我们有两条Follower臂，一条19KG，一条30KG，分别标定后都存储在这个位置。

.. note::

    ``.cache`` 文件在 ``linux`` 的 ``home`` 下默认是隐藏的，使用 ``Ctrl+H`` 使得隐藏文件夹显示出来。

    (base) escommune@ubuntu2403:~/.cache/huggingface/lerobot/calibration/robots/so101_follower$ ls
    **my_19kg_follower_arm.json   my_30kg_follower_arm.json**

Teleoperate [1]_
===========
机械臂连接后，为了降低抖动，会修改舵机默认的PID参数。修改的参数为P(32->16)。 ``so101_follower.py->connect()->configure()``

.. note::

    遥操作默认频率60HZ。加入摄像头后，频率会有所下降。一旦达到20hz，控制频率降低，导致从臂(Follower)会发抖。

无摄像头遥操作。

windows
-------

.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower --robot.port=COM3 --robot.id=my_awesome_follower_arm --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=my_awesome_leader_arm

linux
------
.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower --robot.port=/dev/ttyACM1 --robot.id=my_awesome_follower_arm --teleop.type=so101_leader --teleop.port=/dev/ttyACM0 --teleop.id=my_awesome_leader_arm

Camera [3]_
===========

使用下面的python注册脚本，寻找摄像头。

.. code-block:: console

    lerobot-find-cameras opencv


.. note::

    Windows openCV 多线程有陈年旧bug，只能读一个 [7]_ 。

    Linux可以都执行。Linux两个摄像头不要插在一个hub上(USB控制器上)，否则共用IO带宽，容易出问题。


由于已知的 Windows 平台的问题，多线程读取只能读一个摄像头，第二个就报错。[4]_ [5]_ windows只能单一摄像头。

而且默认代码的单一摄像头读取也可能出现问题。
虽经过 ``pull/1495`` [6]_ 修改后，将OpenCV后端换为 ``cv2.CAP_MSMF``。但并不是所有的windows电脑都被修复。如果你出现类似问题。建议修改为如下

.. code-block:: python

    # Escommune
    # src/lerobot/cameras/utils.py line 71,72
    if platform.system() == "Windows":
        return int(cv2.CAP_DSHOW)  # Use "DSHOW" or "ANY" for Windows instead of MSMF

.. note::

    可以通过下面的代码看自己支持的后端。

    .. code-block:: python

        import cv2
        build_info = cv2.getBuildInformation()

        >>>
        Video I/O backends in this OpenCV build:
        =========================================
          Video I/O:
            FFMPEG:                      YES (prebuilt binaries)
              avcodec:                   YES (58.134.100)
              avformat:                  YES (58.76.100)
              avutil:                    YES (56.70.100)
              swscale:                   YES (5.9.100)
              avresample:                YES (4.0.0)
            GStreamer:                   NO
            DirectShow:                  YES

摄像头参数是python的字典，**每一个空格都很重要**。

.. code-block::

    {
        env: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30, fourcc: 'MJPG'},
        hand: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}
    }

windows
-------

单摄

.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower  --robot.port=COM3 --robot.id=my_awesome_follower_arm --robot.cameras="{ env: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}}" --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=my_awesome_leader_arm --display_data=true


linux
-----

Dual-Cam YUYV(Slow High Quality)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower  \
                        --robot.port=/dev/ttyACM1   \
                        --robot.id=my_awesome_follower_arm \
                        --robot.cameras="{ hand: {type: opencv, index_or_path: 2, width: 640, height: 480, fps: 30, fourcc: 'YUYV'}, env: {type: opencv, index_or_path: 4, width: 640, height: 480, fps: 30, fourcc: 'YUYV'}}"
                        --teleop.type=so101_leader  \
                        --teleop.port=/dev/ttyACM0  \
                        --teleop.id=my_awesome_leader_arm \
                        --display_data=true

Dual-Cam MJPG(Fast Low Quality)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower  \
                        --robot.port=/dev/ttyACM1   \
                        --robot.id=my_awesome_follower_arm \
                        --robot.cameras="{ hand: {type: opencv, index_or_path: 2, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}, env: {type: opencv, index_or_path: 4, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}}"
                        --teleop.type=so101_leader  \
                        --teleop.port=/dev/ttyACM0  \
                        --teleop.id=my_awesome_leader_arm \
                        --display_data=true

.. code-block:: bash

    lerobot-find-cameras
    ERROR:lerobot.scripts.lerobot_find_cameras:Error finding RealSense cameras: name 'rs' is not defined

    --- Detected Cameras ---
    Camera #0:
      Name: OpenCV Camera @ /dev/video0
      Type: OpenCV
      Id: /dev/video0
      Backend api: V4L2
      Default stream profile:
        Format: 0.0
        Fourcc: YUYV
        Width: 640
        Height: 480
        Fps: 30.0
    --------------------
    Camera #1:
      Name: OpenCV Camera @ /dev/video2
      Type: OpenCV
      Id: /dev/video2
      Backend api: V4L2
      Default stream profile:
        Format: 0.0
        Fourcc: YUYV
        Width: 640
        Height: 480
        Fps: 30.0
    --------------------
    Camera #2:
      Name: OpenCV Camera @ /dev/video4
      Type: OpenCV
      Id: /dev/video4
      Backend api: V4L2
      Default stream profile:
        Format: 0.0
        Fourcc: YUYV
        Width: 640
        Height: 480
        Fps: 30.0
    --------------------

    Finalizing image saving...
    Image capture finished. Images saved to outputs/captured_images

    (lerobot) escommune@ubuntu2403:~/lerobot$ lerobot-teleoperate --robot.type=so101_follower  --robot.port=/dev/ttyACM1 --robot.id=my_awesome_follower_arm --robot.cameras="{ hand: {type: opencv, index_or_path: 2, width: 640, height: 480, fps: 30, fourcc: 'YUYV'}, env: {type: opencv, index_or_path: 4, width: 640, height: 480, fps: 30, fourcc: 'YUYV'}}" --teleop.type=so101_leader --teleop.port=/dev/ttyACM0 --teleop.id=my_awesome_leader_arm --display_data=true
    INFO 2026-01-11 18:19:05 eoperate.py:199 {'display_compressed_images': False,
     'display_data': True,
     'display_ip': None,
     'display_port': None,
     'fps': 60,
     'robot': {'calibration_dir': None,
               'cameras': {'env': {'color_mode': <ColorMode.RGB: 'rgb'>,
                                   'fourcc': 'YUYV',
                                   'fps': 30,
                                   'height': 480,
                                   'index_or_path': 4,
                                   'rotation': <Cv2Rotation.NO_ROTATION: 0>,
                                   'warmup_s': 1,
                                   'width': 640},
                           'hand': {'color_mode': <ColorMode.RGB: 'rgb'>,
                                    'fourcc': 'YUYV',
                                    'fps': 30,
                                    'height': 480,
                                    'index_or_path': 2,
                                    'rotation': <Cv2Rotation.NO_ROTATION: 0>,
                                    'warmup_s': 1,
                                    'width': 640}},
               'disable_torque_on_disconnect': True,
               'id': 'my_awesome_follower_arm',
               'max_relative_target': None,
               'port': '/dev/ttyACM1',
               'use_degrees': False},
     'teleop': {'calibration_dir': None,
                'id': 'my_awesome_leader_arm',
                'port': '/dev/ttyACM0',
                'use_degrees': False},
     'teleop_time_s': None}
    INFO 2026-01-11 18:19:05 ader_base.py:77 my_awesome_leader_arm SO101Leader connected.
    INFO 2026-01-11 18:19:06 a_opencv.py:180 OpenCVCamera(2) connected.
    INFO 2026-01-11 18:19:07 a_opencv.py:180 OpenCVCamera(4) connected.
    INFO 2026-01-11 18:19:07 wer_base.py:105 my_awesome_follower_arm SO101Follower connected.
    Teleop loop time: 59.82ms (17 Hz)


Ref
===

.. [1] LeRobot DoC https://huggingface.co/docs/lerobot/so101
.. [2] EsCommune Bilibili https://www.bilibili.com/video/BV1HJBLBuEnU/
.. [3] LeRobot DoC https://huggingface.co/docs/lerobot/cameras#setup-cameras
.. [4] Lerobot GitHub  **BUG** Failed to connect or configure OpenCV camera 0 https://github.com/huggingface/lerobot/issues?q=Failed%20to%20connect%20or%20configure%20OpenCV%20camera%200
.. [5] Lerobot GitHub  **BUG** myanvoos OpenCV camera connection fails on Windows due to default backend https://github.com/huggingface/lerobot/issues/1368
.. [6] Lerobot GitHub todateman pull/1495  https://github.com/huggingface/lerobot/pull/1495
.. [7] OpneCV GitHub **BUG** Windows MultiThread MultiCam https://github.com/opencv/opencv/issues/27312