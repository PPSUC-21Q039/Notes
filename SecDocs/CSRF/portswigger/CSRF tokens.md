在本节中，我们将解释什么是 CSRF 令牌，它们如何防止 CSRF 攻击，以及应该如何生成和验证 CSRF 令牌。
# 什么是CSRF tokens?
CSRF 令牌是一个唯一的、秘密的、不可预测的值，由服务器端应用程序生成并以包含在客户端发出的后续 HTTP 请求中的方式传输到客户端。当发出后面的请求时，服务器端应用程序验证请求是否包含预期的令牌，如果令牌丢失或无效，则拒绝请求。

CSRF 令牌可以防止 CSRF 攻击，因为攻击者无法构建适合提供给受害者用户的完全有效的 HTTP 请求。由于攻击者无法确定或预测用户 CSRF 令牌的值，因此他们无法使用应用程序履行请求所需的所有参数构造请求。
# 如何生成CSRF tokens?
CSRF 令牌应该包含显着的熵并且是高度不可预测的，具有与一般会话令牌相同的属性。 您应该使用加密强度伪随机数生成器 (PRNG)，使用创建时的时间戳和静态密钥作为种子。 如果您需要超出 PRNG 强度的进一步保证，您可以通过将其输出与一些特定于用户的熵连接起来生成单个令牌，并对整个结构进行强散列。这为试图根据发给他们的样本分析代币的攻击者提供了额外的障碍。
# CSRF tokens如何进行传输？
CSRF 令牌应被视为机密，并在其整个生命周期中以安全的方式进行处理。通常有效的方法是在使用 POST 方法提交的 HTML 表单的隐藏字段中将令牌传输给客户端。提交表单时，令牌将作为请求参数包含在内：
```html
<input type="hidden" name="csrf-token" value="CIwNZNlR4XbisJF39I8yWnWX9wX4WFoz" />
```
为提高安全性，包含 CSRF 令牌的字段应尽早放置在 HTML 文档中，最好是在任何非隐藏输入字段之前以及在 HTML 中嵌入用户可控数据的任何位置之前。这缓解了攻击者可以使用精心制作的数据来操纵 HTML 文档并捕获其部分内容的各种技术。

将令牌放入 URL 查询字符串的另一种方法不太安全，因为查询字符串：

- 在客户端和服务器端的不同位置登录；
- 有可能在 HTTP Referer 标头内传输给第三方；和
- 可以在用户浏览器的屏幕上显示。

一些应用程序在自定义请求标头中传输 CSRF 令牌。这为设法预测或捕获另一个用户令牌的攻击者提供了进一步的防御，因为浏览器通常不允许跨域发送自定义标头。但是，该方法将应用程序限制为使用 XHR（而不是 HTML 表单）发出受 CSRF 保护的请求，并且在许多情况下可能被认为过于复杂。

CSRF 令牌不应在 cookie 中传输。
# 如何验证CSRF tokens？
当生成 CSRF 令牌时，它应该存储在服务器端的用户会话数据中。当接收到需要验证的后续请求时，服务器端应用程序应验证该请求是否包含与存储在用户会话中的值匹配的令牌。无论请求的 HTTP 方法或内容类型如何，都必须执行此验证。如果请求根本不包含任何令牌，则应该以与存在无效令牌时相同的方式拒绝它。
