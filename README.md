# MindSaver 的技术笔记

一个只放文字的技术博客。Hugo + PaperMod，静态生成，无成本无依赖。

设计原则：**内容比界面重要**。白底、单栏、无卡片、无配图，  
每篇文章的元信息只有日期、阅读时长和标签。

## 快速开始

```bash
# 启动本地预览（改文件自动刷新），浏览器打开 http://localhost:1313
hugo server

# 正式构建，产物在 public/
hugo --minify

# 带草稿预览
hugo server -D
```

> **如果提示「此应用无法在你电脑运行」**
> 说明 PATH 里指向了一个损坏的 hugo.exe。检查一下：
>
> ```bash
> where hugo
> ```
>
> 如果指向 `WinGet\Links\hugo.exe`，把它删掉，然后把真实安装目录加进 PATH：
>
> ```text
> C:\Users\BISSE\AppData\Local\Microsoft\WinGet\Packages\Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe
> ```
>
> 改完 PATH 需要重开命令行窗口才生效。


## 写一篇新文章

在 `content/posts/` 下新建 `.md` 文件，文件名会成为 URL 的一部分，  
建议用英文短名（如 `my-first-post.md`）。

```markdown
---
title: "文章标题"
date: 2026-10-04T20:30:00+08:00
draft: false
tags: ["Hugo", "建站"]
categories: ["技术"]
description: "一句话摘要，显示在列表页。"
toc: true
---

正文从这里开始，支持全部 Markdown 语法。
```

字段说明：

| 字段            | 必填 | 说明                     |
| :------------ | :- | :--------------------- |
| `title`       | 是  | 文章标题                   |
| `date`        | 是  | 发布时间，用 ISO 格式          |
| `draft`       | 是  | `true` 时不进入正式构建        |
| `tags`        | 否  | 标签，用于 `/tags/` 页       |
| `categories`  | 否  | 分类，用于 `/categories/` 页 |
| `description` | 否  | 列表页显示的摘要               |
| `toc`         | 否  | `true` 时文章顶部显示目录       |

用命令快速创建：

```bash
hugo new posts/我的新文章.md
```

## 提示块

用 shortcode，三种类型：`tip`（提示）、`note`（注意）、`warning`（警告）。

```markdown
{{< notice tip >}}
这里是提示内容，支持 **Markdown** 和 `代码`。
{{< /notice >}}
```

## 站点结构

```text
content/
├── _index.md            首页配置（标题、是否输出搜索索引）
├── posts/               文章
│   └── _index.md        文章列表页
├── archives/_index.md   归档页（按年月两级分组）
├── tags/_index.md       标签索引
├── categories/_index.md 分类索引
├── search.md            站内搜索页
└── about.md             关于页

layouts/
├── home.html            首页模板（纯文字文章列表）
├── index.json           全站搜索索引
└── _shortcodes/
    └── notice.html      提示块

assets/css/extended/
└── reading.css          全部自定义样式（覆盖主题默认外观）

tools/
└── preview.py           生成可离线浏览的预览副本
```

## 常用配置

改 `hugo.toml`：

```toml
# 站点标题和地址
title = 'MindSaver 的技术笔记'
baseURL = 'https://你的域名/'

# 首页显示多少篇文章（留空/0 = 全部）
homePostsCount = 10
```

其他常用开关：

| 配置                          | 作用                                   |
| :-------------------------- | :----------------------------------- |
| `params.DateFormat`         | 日期格式，如 `'2006年1月2日'`                 |
| `params.ShowToc`            | 全局默认是否显示目录                           |
| `params.ShowCodeCopyButton` | 代码块复制按钮                              |
| `params.defaultTheme`       | `'auto'`（跟随系统）或 `'light'` / `'dark'` |
| `params.disableThemeToggle` | `true` 隐藏深色模式切换按钮                    |
| `params.author`             | 页脚显示的作者名                             |
| `permalinks.posts`          | 文章 URL 结构                            |

## 离线预览

`public/` 里的资源用的是绝对路径，直接双击 `index.html` 会丢样式。  
用这个脚本生成一份相对路径的副本，可以直接用浏览器打开：

```bash
python tools/preview.py            # 生成到系统临时目录
python tools/preview.py --serve    # 顺便起本地服务并自动开浏览器
```

## 发布

构建产物是纯静态文件，`public/` 整个目录传到任意静态托管即可：

- **GitHub Pages**：推到仓库后在 Settings → Pages 里选 `main` 分支根目录
- **Gitee Pages**：同上，仓库设置里开启
- **Vercel / Netlify**：连仓库，构建命令填 `hugo --minify`，输出目录填 `public`
- **国内服务器 / 对象存储**：直接传 `public/` 目录

⚠️ 发布前记得把 `hugo.toml` 里的 `baseURL` 改成真实域名，否则链接和 RSS 会指向错误地址。

## 关于主题

PaperMod 以 MIT 协议发布。页脚保留了 `Powered by Hugo & PaperMod` 署名，  
建议保留 —— 这是对开源作者的尊重，也能帮他们获得曝光。
