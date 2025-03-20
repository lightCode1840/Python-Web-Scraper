import requests
from bs4 import BeautifulSoup
import html2text  # 需要安装：pip install html2text
import re


def html_to_markdown(html):
    """智能转换HTML到Markdown格式"""
    converter = html2text.HTML2Text()
    converter.body_width = 0  # 禁用自动换行
    converter.ignore_links = False  # 保留链接
    converter.mark_code = True  # 高亮代码块
    return converter.handle(html)


def crawl_to_markdown(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://xiaolincoding.com/"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'

        if response.status_code != 200:
            raise Exception(f"请求失败，状态码：{response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # 精准定位内容区域（根据目标站点的class调整）
        main_content = soup.find('div', class_='theme-default-content')
        if not main_content:
            raise Exception("内容区域定位失败")

        # 清理无用元素
        for tag in ['script', 'style', 'footer', 'nav', 'aside', 'header']:
            for element in main_content.find_all(tag):
                element.decompose()

        # 转换到Markdown
        md_content = html_to_markdown(str(main_content))

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

if __name__ == '__main__':
    # 使用示例
    # target_url = "https://xiaolincoding.com/interview/java.html"
    target_url = "https://xiaolincoding.com/interview/juc.html"
    
    crawl_to_markdown(target_url)