一些网站使用 SameSite cookie 防御 CSRF 攻击。<br />SameSite 属性可用于控制是否以及如何在跨站点请求中提交 cookie。通过设置会话 cookie 的属性，应用程序可以阻止默认浏览器行为，即自动将 cookie 添加到请求中，无论它们来自何处。<br />当服务器发出 cookie 时，SameSite 属性被添加到 Set-Cookie 响应标头中，并且该属性可以被赋予两个值，Strict 或 Lax。例如：
```
Set-Cookie: SessionId=sYMnfCUrAlmqVVZn9dqevxyFpKZt30NN; SameSite=Strict;
```
```
Set-Cookie: SessionId=sYMnfCUrAlmqVVZn9dqevxyFpKZt30NN; SameSite=Lax;
```
如果 SameSite 属性设置为 Strict，则浏览器将不会在来自其他站点的任何请求中包含 cookie。这是最具防御性的选项，但它会损害用户体验，因为如果登录用户点击第三方链接到某个站点，那么他们将显示为未登录，并且需要再次登录才能以正常方式与网站交互。

如果 SameSite 属性设置为 Lax，则浏览器将在来自另一个站点的请求中包含 cookie，但前提是满足两个条件：

- 该请求使用 GET 方法。使用其他方法（例如 POST）的请求将不包含 cookie。
- 该请求来自用户的顶级导航，例如单击链接。其他请求，例如由脚本发起的请求，将不包含 cookie。

在 Lax 模式下使用 SameSite cookie 确实提供了对 CSRF 攻击的部分防御，因为作为 CSRF 攻击目标的用户操作通常使用 POST 方法实现。这里有两个重要的警告是

- 一些应用程序确实使用 GET 请求来实现敏感操作。
- 许多应用程序和框架都可以容忍不同的 HTTP 方法。在这种情况下，即使应用程序本身设计为使用 POST 方法，它实际上也会接受切换为使用 GET 方法的请求。

由于上述原因，不建议仅依靠 SameSite cookie 来防御 CSRF 攻击。但是，与 CSRF token结合使用时，SameSite cookie 可以提供额外的防御层，可以减轻基于token的防御中的任何缺陷。
