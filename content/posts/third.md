---
title: "Markdown 排版备忘"
date: 2026-08-30T15:20:00+08:00
draft: false
tags: ["Markdown", "工具链"]
categories: ["技术"]
description: "写作常用的 Markdown 语法速查，含数学公式、提示块、代码高亮。"
summary: "一篇用来对照的语法速查表。"
toc: true
---

写博客常用的语法基本就这些，够用了。

## 基础

```markdown
**粗体**  *斜体*  `行内代码`

# 一级标题
## 二级标题
### 三级标题

> 引用
> 多行也是

- 无序列表
- 第二项
  - 嵌套项

1. 有序列表
2. 第二项

[链接文字](https://example.com)
![图片描述](/images/a.png "可选标题")
```

## 表格

| 左列 | 中列 | 右列 |
|:-----|:----:|------:|
| 1    | 2    | 3     |
| 左对齐 | 居中 | 右对齐 |

## 代码块

指定语言就会自动高亮：

```java
public static void main(String[] args) {
    System.out.println("hello, world");
}
```

```python
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

不指定语言就是纯文本：

```
这是一段纯文本
```

## 数学公式

行内公式：`$E = mc^2$`

独立成行的：

$$
\frac{\partial \mathcal{L}}{\partial w} = 0
$$

## 提示块

Papermod 支持这种扩展语法：

{{< notice tip >}}
这是提示（TIP），**支持加粗**和 `代码`。
{{< /notice >}}

{{< notice note >}}
这是注意（NOTE）。
{{< /notice >}}

{{< notice warning >}}
这是警告（CAUTION）。
{{< /notice >}}

## 分割线

---

## 图片尺寸控制

```markdown
![描述](image.png =300x)
```

后面的 `=300x` 是 PaperMod 的扩展，会限制显示宽度。

## 脚注

```markdown
脚注的写法[^1]。

[^1]: 这里是脚注内容。
```
