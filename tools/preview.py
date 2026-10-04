#!/usr/bin/env python
"""
本地预览辅助脚本。

Hugo 生成的 public/ 里，CSS/图片都用绝对路径（/assets/...）引用，
直接双击 public/index.html 用 file:// 打开会丢样式（绝对路径解析不到）。

本脚本把构建产物复制一份到临时目录，把资源引用改成相对路径并去掉
SRI 校验（file:// 下 integrity 会校验失败导致浏览器拒载 CSS），
这样就能用浏览器直接打开预览，不需要起本地服务器。

用法：
    python tools/preview.py            # 生成预览到系统临时目录并打印路径
    python tools/preview.py --serve    # 生成后顺便起一个本地 http 服务
"""

import argparse
import http.server
import os
import re
import shutil
import socketserver
import sys
import tempfile
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

# 只改写静态资源前缀，正文里的 /posts/... 等站内链接保持原样（file:// 下也能跳）
ASSET_RE = re.compile(r'(href|src)=(https?://[^/"\']+)?(/(?:assets|favicon|apple-touch-icon|sitemap|index\.json)[^"\'\s>]*)')
INTEGRITY_RE = re.compile(r'\s+(integrity="[^"]*"|crossorigin=anonymous)')
CANONICAL_RE = re.compile(r'<link rel=canonical[^>]*>')


def rewrite_html(path: Path, depth: int) -> None:
    """把绝对资源路径改成相对路径，并去掉 file:// 下会失败的 SRI 校验。"""
    text = path.read_text(encoding="utf-8")
    prefix = "./" if depth == 0 else "../" * depth

    def fix(m):
        # 保留已有的完整 URL（外部资源），只改站内绝对路径
        if m.group(2):
            return m.group(0)
        return f"{m.group(1)}={prefix}{m.group(3).lstrip('/')}"

    new = ASSET_RE.sub(fix, text)
    new = INTEGRITY_RE.sub("", new)
    new = CANONICAL_RE.sub("", new)
    if new != text:
        path.write_text(new, encoding="utf-8")


def build_preview(dest: Path) -> None:
    if not PUBLIC.exists():
        sys.exit("public/ 不存在，请先运行 hugo build")

    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(PUBLIC, dest)

    for html in dest.rglob("*.html"):
        rel = html.relative_to(dest).parent
        depth = 0 if str(rel) == "." else len(rel.parts)
        rewrite_html(html, depth)


def serve(directory: Path, port: int) -> None:
    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(  # noqa: E731
        *a, directory=str(directory), **kw
    )
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        url = f"http://127.0.0.1:{port}/"
        print(f"服务已启动：{url}")
        print("按 Ctrl+C 停止")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        httpd.serve_forever()


def main() -> None:
    ap = argparse.ArgumentParser(description="生成可离线浏览的本地预览")
    ap.add_argument("--serve", action="store_true", help="顺便启动本地 http 服务")
    ap.add_argument("--port", type=int, default=8899, help="服务端口，默认 8899")
    ap.add_argument("--out", default=None, help="预览输出目录，默认为临时目录")
    args = ap.parse_args()

    dest = Path(args.out) if args.out else Path(tempfile.gettempdir()) / "blog-preview"
    build_preview(dest)
    print(f"预览文件已生成：{dest}")

    if args.serve:
        serve(dest, args.port)
    else:
        index = dest / "index.html"
        print(f"用浏览器打开：{index}")


if __name__ == "__main__":
    main()
