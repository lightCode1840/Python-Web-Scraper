import re

import requests
from bs4 import BeautifulSoup
import html2text
import random
import time
import chardet

# 配置随机请求头（参考网页7）
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15..."
]


def html_to_md(html_content):
    """HTML转Markdown（参考网页7/9）"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    return h.handle(html_content)


def crawler(url):
    try:
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://javabetter.cn/'
        }

        with requests.Session() as s:
            response = s.get(url, headers=headers, timeout=15)
            # 动态编码检测
            raw_data = response.content
            detected_encoding = chardet.detect(raw_data)['encoding']
            response.encoding = detected_encoding if detected_encoding else 'utf-8'

        soup = BeautifulSoup(response.content.decode(response.encoding, errors='ignore'), 'html.parser')

        # 后续内容提取逻辑保持不变...

        # 正确的主内容选择器（根据提供的HTML）
        main_content = soup.find('main', {'id': 'main-content'})

        # 备用选择器（文章内容区域）
        if not main_content:
            main_content = soup.find('div', class_='theme-hope-content')

        if not main_content:
            raise ValueError("需检查动态加载内容或更新选择器")

        # 格式转换
        md_content = html_to_md(str(main_content))
    #
    #     # 保存文件
    #     with open('output.md', 'w', encoding='utf-8') as f:
    #         f.write(f"# {soup.title.string}\n\n")
    #         f.write(md_content)
    #
    #     print("抓取成功！文件已保存为output.md")
    #
    # except Exception as e:
    #     print(f"抓取失败：{str(e)}")
    #
    #     # 转换到Markdown
    #     md_content = html_to_markdown(str(main_content))

        # 增强代码块格式化（针对技术文档优化）
        md_content = re.sub(r'```(\w+)?\n', lambda m: f"```{m.group(1) or 'text'}\n", md_content)

        # 生成文件名
        filename = url.split('/')[-1].replace('.html', '.md')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {soup.title.text}\n\n")
            f.write(f"源地址：[{url}]({url})\n\n")
            f.write(md_content)

        print(f"Markdown已保存到：{filename}")

    except Exception as e:
        print(f"错误：{str(e)}")


# def crawler(url):
#     try:
#         # 1.发送请求（参考网页2/3）
#         headers = {'User-Agent': random.choice(USER_AGENTS)}
#         response = requests.get(url, headers=headers, timeout=10)
#         response.raise_for_status()
#
#         # 2.解析内容（根据网页结构调整选择器）
#         soup = BeautifulSoup(response.text, 'html.parser')
#         main_content = soup.find('article')  # 根据目标网页结构调整
#
#         if not main_content:
#             raise ValueError("未找到文章主体内容")
#
#         # 3.格式转换
#         md_content = html_to_md(str(main_content))
#
#         # 4.保存文件（参考网页7）
#         with open('output.md', 'w', encoding='utf-8') as f:
#             f.write(f"# {soup.title.string}\n\n")
#             f.write(md_content)
#
#         print("抓取成功！文件已保存为output.md")
#
#     except Exception as e:
#         print(f"抓取失败：{str(e)}")


if __name__ == '__main__':
    target_url = "https://javabetter.cn/sidebar/sanfene/linux.html"
    crawler(target_url)
    time.sleep(2)  # 设置请求间隔