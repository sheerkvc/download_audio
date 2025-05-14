# YouTube视频转音频命令行脚本

利用yt-dlp写了个简单脚本，来下载视频转为.mav格式音频（纯自用，没技术，是小白）

#### 1、虚拟环境

1、python3 -m venv venv    # 创建自己的虚拟环境（名字随便）

2、source venv/bin/activate  # 激活它

3、pip install -r requirements.txt # 安装依赖（其实也没啥依赖doge）

#### 2、编写cookie文件

把自己cookie的一部分存在y2b_cookie.txt里，参考文件内的示例，不懂的gpt就可以，这个挺容易

#### 3、编写video_link文件

把要下载的视频链接粘贴过来，每行一个，按文件中的示例

#### 4、原神，启动！

启动脚本：python download_audio.py

#### 5、退出虚拟环境（没太大必要）

终端输入：deactivate
