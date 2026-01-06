*******
Scripts
*******

.. note::

    Mainly for windows. If you want to operate at LinuxOS, please check the Ref [1]_.

find-port [1]_
=========

插入端口，所有已插入的端口都会被脚本识别。

拔出想要知道端口号的端口，键入enter。

.. code-block:: console

    lerobot-find-port

setup-motors [1]_
============

多个舵机使用串行通讯挂在一条舵机总线上(一条线)。通过不同的ID区分。其中 Gripper 的 ID 为6，依次递减。

.. code-block:: console

    lerobot-setup-motors --robot.type=so101_follower --robot.port=COM3

.. code-block:: console

    lerobot-setup-motors --teleop.type=so101_leader --teleop.port=COM4

calibrate [1]_ [2]_
=========

舵机是绝对值磁编码传感器，掉电后角度不丢失。可以360度旋转 即 0-4095（0-360）。

舵机的中点 2048 需要 与 物理结构对应。所以要标定中点（修改中点偏移量）。

结构件安装后，旋转范围有了物理限制。以标定中点为中心点，设置角度限制。

.. warning::

    **尽量使舵机标定的角度限制与物理限制贴合，否则掉电后对机械臂的操作可能超过标定的范围，会出问题！！！**

.. code-block:: console

    lerobot-calibrate  --robot.type=so101_follower --robot.port=COM3 --robot.id=my_awesome_follower_arm # <- Give the robot a unique name

.. code-block:: console

    lerobot-calibrate  --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=my_awesome_leader_arm # <- Give the robot a unique name



teleoperate [1]_
===========

无摄像头遥操作

.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower --robot.port=COM3 --robot.id=my_awesome_follower_arm --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=my_awesome_leader_arm


camera [3]_
------
由于已知的Windows平台 openCV backend 的问题. [4]_ [5]_

虽经过 ``pull/1495`` [6]_ 修改后，换为 ``cv2.CAP_MSMF``。但并不是所有的windows电脑都被修复。如果你出现类似问题。建议修改为如下

.. code-block:: python

    # Escommune
    # src/lerobot/cameras/utils.py line 71,72
    if platform.system() == "Windows":
        return int(cv2.CAP_ANY)  # Use Any for Windows instead of MSMF

.. code-block:: console

    lerobot-find-cameras opencv

双摄像头遥操作

.. code-block::

    {
        hand: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30, fourcc: 'MJPG'},
        env: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}
    }


.. code-block:: console

    lerobot-teleoperate --robot.type=so101_follower  --robot.port=COM3 --robot.id=my_awesome_follower_arm --robot.cameras="{ hand: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}, env: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30, fourcc: 'MJPG'}}" --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=my_awesome_leader_arm --display_data=true


Ref
===

.. [1] LeRobot DoC https://huggingface.co/docs/lerobot/so101
.. [2] EsCommune Bilibili https://www.bilibili.com/video/BV1HJBLBuEnU/
.. [3] LeRobot DoC https://huggingface.co/docs/lerobot/cameras#setup-cameras
.. [4] Failed to connect or configure OpenCV camera 0 https://github.com/huggingface/lerobot/issues?q=Failed%20to%20connect%20or%20configure%20OpenCV%20camera%200
.. [5] myanvoos OpenCV camera connection fails on Windows due to default backend https://github.com/huggingface/lerobot/issues/1368
.. [6] todateman pull/1495  https://github.com/huggingface/lerobot/pull/1495