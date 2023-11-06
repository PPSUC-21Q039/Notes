# 什么是XML？
XML 代表“可扩展标记语言”。 XML 是一种设计用于存储和传输数据的语言。与 HTML 一样，XML 使用标签和数据的树状结构。与 HTML 不同，XML 不使用预定义的标签，因此可以为标签指定描述数据的名称。在 Web 历史的早期，XML 作为一种数据传输格式很流行（“AJAX”中的“X”代表“XML”）。但它的受欢迎程度现在已经下降，现在更为偏爱 JSON 格式。
# 什么是XML实体？
XML 实体是一种在 XML 文档中表示数据项的方式，而不是使用数据本身。 XML 语言的规范中内置了各种实体。例如，实体 &lt; 和 &gt; 表示字符 < 和 >。这些是用于表示 XML 标记的元字符，因此当它们出现在数据中时，通常必须使用它们的实体来表示。
# 什么是文档类型定义？
XML document type definition (DTD) 包含可以定义 XML 文档的结构、它可以包含的数据值的类型以及其他项的声明。 DTD 在 XML 文档开头的可选 DOCTYPE 元素中声明。 DTD 可以完全独立于文档本身（称为“内部 DTD”），也可以从其他地方加载（称为“外部 DTD”），也可以是两者的混合。
# 什么是XML自定义实体
XML 允许在 DTD 中定义自定义实体。例如：
```xml
<!DOCTYPE foo [ <!ENTITY myentity "my entity value" > ]>
```
这个定义意味着实体引用 &myentity; 的任何用法。 XML 文档中的值将被替换为定义的值："my entity value"。
# 什么是 XML 外部实体？
XML 外部实体是一种自定义实体，其定义位于声明它们的 DTD 之外。<br />外部实体的声明使用 SYSTEM 关键字，并且必须指定应该从中加载实体值的 URL。例如:
```xml
<!DOCTYPE foo [ <!ENTITY ext SYSTEM "http://normal-website.com" > ]>
```
URL 可以使用 file:// 协议，因此可以从文件加载外部实体。例如：
```xml
<!DOCTYPE foo [ <!ENTITY ext SYSTEM "file:///path/to/file" > ]>
```
XML 外部实体提供了 XML 外部实体攻击发生的主要方式。
