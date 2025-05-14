import os
import subprocess
from PIL import Image

# 读取txt文件中的视频链接
def read_video_links(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# 下载音频和封面
def download_audio_and_cover(video_url, output_dir):
    # 下载音频为WAV格式
    audio_output = os.path.join(output_dir, '%(title)s.%(ext)s')
    subprocess.run([
        'yt-dlp',
        '-x',  # 提取音频
        '--audio-format', 'wav',  # 指定音频格式为WAV
        '-o', audio_output,  # 输出文件名
        video_url
    ])

    # 下载封面
    cover_output = os.path.join(output_dir, 'cover.%(ext)s')
    subprocess.run([
    'yt-dlp',
    '--cookies-from-browser', 'chrome',  # 或 'firefox' 
    '-x',  # 提取音频
    '--audio-format', 'wav',  # 指定音频格式为 WAV
    '-o', audio_output,  # 输出文件名
    video_url
])

    # 查找下载的封面文件
    cover_files = [f for f in os.listdir(output_dir) if f.startswith('cover.')]
    if cover_files:
        cover_file = os.path.join(output_dir, cover_files[0])
        if cover_file.endswith('.webp'):
            # 将WebP转换为PNG
            png_file = cover_file.replace('.webp', '.png')
            img = Image.open(cover_file).convert("RGB")
            img.save(png_file, "png")
            os.remove(cover_file)  # 删除原始的WebP文件

# 主函数
def main():
    # 读取video_link.txt中的链接
    video_links = read_video_links('video_link.txt')

    # 创建输出目录
    output_dir = 'downloads'
    os.makedirs(output_dir, exist_ok=True)

    # 下载每个视频的音频和封面
    for link in video_links:
        download_audio_and_cover(link, output_dir)

if __name__ == '__main__':
    main()