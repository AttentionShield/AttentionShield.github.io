---
title: "用 Hugo + PaperMod 搭一个只放文字的博客"
date: 2026-10-04T20:30:00+08:00
draft: false
tags: ["Hugo", "建站", "工具链"]
categories: ["技术"]
description: "为什么做这个站，以及它长什么样。顺便把一堆踩坑记下来。"
summary: "把一个杂乱的数字花园砍成一张白纸的过程。"
toc: true
---

博客这东西，很容易越做越重。

一开始想加评论系统，加了统计代码，加了动态背景，加了翻页动画，加了一堆花哨的图标。三个月后回头看，主页上全是"东西"，唯独没有内容本身。于是我把它砍了，重新搭了一遍。

## 我想要的到底是什么

四个要求，很朴素：

1. **打开就是文字**。不要大图、不要轮播、不要"欢迎来到我的小站"配一张风景照。
2. **能找到旧文章**。按年月归档，十年后还能翻回去。
3. **写起来不费劲**。会用 Markdown 就能写，不用学新东西。
4. **不花钱**。静态生成，扔哪都能跑。

Hugo 的 PaperMod 主题几乎是这个清单的标准答案，所以没什么好犹豫的。

## 站点结构

最终就是这几个页面：

```text
/posts/       文章列表
/archives/    按年月分组归档
/tags/        标签索引
/about/       关于
```

没有别的了。

### 归档页长什么样

参考站点最聪明的地方在于它用**两级分组 + 一行元信息**做索引：

```text
2026  2

  October  1
    用 Hugo + PaperMod 搭一个只放文字的博客
    2026年10月4日 · 8 分钟
```

年份下面挂月份，月份下面挂文章，每篇只带日期和阅读时长。眼睛可以竖着扫，不用横向读卡片。

{{< notice tip >}}
这个结构是 PaperMod 内置的，不用自己写模板。开一下归档页的 `layout: archives` 就有。
{{< /notice >}}

## 一些配置细节

Hugo 现在用 `hugo.toml` 了。核心的几项：

```toml
[params]
mainSections = ['posts']
ShowReadingTime = true
ShowToc = true
ShowBreadCrumbs = false         # 不要面包屑
disableAnchoredHeadings = true  # 标题旁边不要 #
DateFormat = '2006年1月2日'
```

`disableAnchoredHeadings` 这个开关很多人不知道，设成 `true` 之后 `## 标题` 旁边不会冒出 `#`，页面干净很多。

### 中文要注意的

日期格式用 Go 的时间格式模板，`2006年1月2日` 这种直接写就行。想显示英文月名就用 `January 2, 2006`。

字体我换成了这套栈：

```text
system-ui, -apple-system, "Segoe UI", "Microsoft YaHei",
"PingFang SC", "Noto Sans CJK SC", sans-serif
```

Windows 上的实际渲染会落到微软雅黑，苹果上落到苹方，都挺好看。

## 一点小麻烦

踩到的坑记一下：

- Hugo 从 v0.158 起 `languageCode` 废弃了，改用 `locale`，不改每次构建都会 WARN。
- Windows 下从 `WinGet\Links` 调 `hugo` 有时候不出声，得用 `Packages` 里的真实路径。
- GitHub 上 PaperMod 默认分支是 `master`，`git submodule add -b main` 会报错。

{{< notice note >}}
`content/` 目录里 `.md` 文件的**文件名**会成为 URL 的一部分，取个英文短名最省事。
{{< /notice >}}

## 结语

技术栈的选择会过时，但"把东西删掉"的决定不会。

> 好的工具不是让你有更多选择，而是让你更少犹豫该选哪个。

这篇本身就是最好的例子——它讲的就是"少即是多"，所以它也没多少内容。

## 延伸

- [Hugo 官方文档](https://gohugo.io/documentation/)
- [PaperMod 主题参数说明](https://github.com/adityatelange/hugo-PaperMod)
- [Learn Git Branching](https://learngitbranching.js.org/) —— Git 可视化学习
