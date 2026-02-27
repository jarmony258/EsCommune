*******
Train
*******

训练一个AI模型最重要的就是数据。为了更好的体验效果，需要自己录制数据集。录制的数据集默认需要上传的Hugging Face。所以需要注册Hugging Face账号。

Hugging Face平台的注册对于注册的网络IP地址有地理位置限制。最好是使用US(American)的地理位置。

注册完成后需要申请 Access Token，这东西只出现一次，记得保存好。通过这个token可以在命令行中访问自己的HF账号的数据。

.. code-block:: console

    # eg. huggingface-cli login --token hf_dfhidhdihsidhfdDjk --add-to-git-credential
    huggingface-cli login --token ${HUGGINGFACE_TOKEN} --add-to-git-credential

HF＿USER
========

windows与linux的 ``$HF_USER`` 的命令有区分。

win-PowerShell
--------------

.. code-block:: console

    $output = hf auth whoami
    $HF_USER = ($output -split ' ')[2]
    echo $HF_USER

linux
-----

.. code-block:: console

    HF_USER=$(hf auth whoami | head -n 1)
    echo $HF_USER

Ref
===

.. [1] LeRobot DoC "Imitation Learning on Real-World Robots" https://huggingface.co/docs/lerobot/il_robots
