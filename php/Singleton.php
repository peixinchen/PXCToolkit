<?php

class Singleton
{
    private static $_instances = array();

    private static function create_instance($class, $arguments)
    {
        $rins = new ReflectionClass($class);
        $instance = $rins->newInstanceArgs($arguments);

        return $instance;
    }

    public static function instance($class, $arguments = array())
    {
        $key = $class . "(" . var_export($arguments, true) . ")";
        if (isset(self::$_instances[$key]) === false) {
            self::$_instances[$key] = self::create_instance($class, $arguments);
        }

        return self::$_instances[$key];
    }
}

class C
{
    ...
}

Singleton::instance(C);
Singleton::instance(C, array($arg1, ...));
