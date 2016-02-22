Title: PHP单例模式的实现
Date: 2016-02-22 18:15
Tags: php 设计模式
Category: php

其实php的单例模式要比python或者其他语言的作用要小得多，主要原因应该是因为php并不常驻内存，因此单例的作用范围仅限于一次请求。不过对于数据库连接这种，实现单例还是有那么一些必要的，下面简单讲一下php实现单例的几种思路：

## 方法1

```php
<?php

class Singleton {

    private static $instance;

    protected function __construct() {}

    public static function getInstance() {
        if(is_null(self::$instance)) {
            self::$instance = new self;

        }
        return self::$instance;
    }
}
```
这个方法的缺点显而易见，不能继承，每个需要单例的类都要写这些代码，并不方便维护

然而如果php版本<5.3，貌似也只能这样了

## 方法2

```php
<?php

class Singleton {

    protected static $instance;

    protected function __construct() {}

    public function __clone() {
        die('clone method is not allowed');
    }

    public static final function getInstance() {
        if(is_null(static::$instance)) {
            static::$instance = new static;

        }
        return static::$instance;
    }

}
```
这里主要利用了php 5.3的后期静态绑定特性，可以得到函数调用时的class，也就允许子类继承Singleton实现单例了，然而由于$instance方法是protected的，不知情的同学可能会复写子类中的$instance方法，造成奇怪的bug，因此也不是什么完美的方案。

## 方法3

```php
<?php

class Singleton {

    private static $instances = array();

    protected function __construct() {}

    public function __clone() {
        die('clone method is not allowed');
    }

    public static final function getInstance() {
        $c = get_called_class();
        if(!isset(self::$instances[$c])) {
            self::$instances[$c] = new $c;

        }
        return self::$instances[$c];
    }

}
```
这里主要利用了php 5.3的新特性get_called_class，可以获取被调用方法所在的类名，从而将实例化后的$instance存在父类中的private属性中，解决了$instance被子类复写的问题。

然而php只能继承一个类，这个方法的缺点也是显而易见的，占用了唯一的父类，因此也并不是完美的解决方案。

## 方法4

```php
<?php

trait Singleton {

    private static $instance;

    public function __clone() {
        die('clone method is not allowed');
    }

    public static final function getInstance() {
        if(is_null(self::$instance)) {
            self::$instance = new self;
        }
        return self::$instance;

    }

}
```
这里则是用到了php 5.4的trait特性，不占用继承的位置了，然而$instance会被子类复写的问题又回来了><

所以看上去php并不能找到一个完美的单例模式实现...
