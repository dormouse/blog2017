+++
date = "2017-01-18T16:36:45+08:00"
title = "golang exercises"
description = "Exercises for golang"
tags  = ["golang", "exercises"]
categories = ["development"]
+++

# fibonacci

``` go
package main

import "fmt"

// fibonacci 函数会返回一个返回 int 的函数。
func fibonacci() func() int {
    count := 0
    a := 1
    b := 1
    return func() int {
        count++
        if count <= 2 {
            a = 1
            b = 1
            return 1
        }
        c := b
        b = a + b
        a = c
        return b
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
```
