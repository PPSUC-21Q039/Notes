### cppdbg

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb)Launch",
            "type": "cppdbg",
            "program": "/usr/local/bin/php",
            "args": ["-S", "0.0.0.0:8080", "-t", "/var/www/html"],
            "stopAtConnect": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable gdb",
                    "text": "-enable",
                    "ignoreFailures": true
                }
            ]
        }

    ]
}
```

