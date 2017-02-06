+++
date  = "2017-01-18T11:56:48+08:00"
title = "Go Quick Start"
description = "Quick Start for golang"
tags  = [ "Development", "Golang"]
draft = true
+++

# Quick Start

## ubuntu

Install golang:
```
sudo apt-get install golang
mkdir -p $HOME/go_work/src/github.com/username/hello
export GOPATH=$HOME/work
```

For convenience, add the workspace's bin subdirectory to your .bashrc:
```
export GOPATH=$HOME/go_work
export PATH=$PATH:$GOPATH/bin
```

Save following to `$GOPATH/src/github.com/username/hello/hello.go`
```
package main

import "fmt"

func main() {
    fmt.Printf("hello, world\n")
}
```

compile and run：
```
go install github.com/username/hello
$GOPATH/bin/hello
```

Done!

# Study source
- [Golang tour (Simple Chinese)](https://tour.go-zh.org/list)
- [Golang document](https://golang.org/doc/)
