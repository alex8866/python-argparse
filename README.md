# Python argparse学习

# 使用argparse步骤

1. 创建一个解析器对象

```python
import argparse
parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')
```

2. 定义参数parse.add_argument()

如果没有指定dest, 则值store在aaa(--aaa), a(-a)中
也就是指定顺序dest > -- > -

3. 解析一个命令行

定义了所有参数之后，你就可以给 parse_args() 传递一组参数字符串来解析命令行。默认情况下，参数是从 sys.argv[1:] 中获取，但你也可以传递自己的参数列表。

parse_args() 的返回值是一个命名空间，包含传递给命令的参数。该对象将参数保存其属性，因此如果你的参数 dest 是 "myoption"，那么你就可以args.myoption 来访问该值。


# 参数动作

**store**: 保存参数值，默认动作
**store_const** 保存一个被定义为参数规格一部分的值，而不是一个来自参数解析而来的值。这通常用于实现非布尔值的命令行标记。
**store_true/store_false** 保存相应的布尔值。这两个动作被用于实现布尔开关。
**append** 将值保存到一个列表中。若参数重复出现，则保存多个值。
**append_const** 将一个定义在参数规格中的值保存到一个列表中。
**version** 打印关于程序的版本信息，然后退出

# Automatically Generated Options

argparse will automatically add options to generate help and show the version information for your application, if configured to do so.

The add_help argument to ArgumentParser controls the help-related options.

# Argument Groups

argparse combines the argument definitions into “groups.” By default, it uses two groups, with one for options and another for required position-based arguments.

argparse能将参数定义组合成“群组”。默认情况下是使用两个群组，一个是选项的群组，另一个是必须的与位置相关的参数群组。

# Mutually Exclusive Options

# Nesting Parsers

The parent parser approach described above is one way to share options between related commands. An alternate approach is to combine the commands into a single program, and use subparsers to handle each portion of the command line. The result works in the way svn, hg, and other programs with multiple command line actions, or sub-commands, does.

# Variable Argument Lists

You can configure a single argument defintion to consume multiple arguments on the command line being parsed. Set nargs to one of these flag values, based on the number of required or expected arguments:
N 	The absolute number of arguments (e.g., 3).
? 	0 or 1 arguments
* 	0 or all arguments
+ 	All, and at least one, argument

# Argument Type

argparse treats all argument values as strings, unless you tell it to convert the string to another type. The type parameter to add_argument() expects a converter function used by the ArgumentParser to transform the argument value from a string to some other type.



# Reference

+ [argparse – Command line option and argument parsing](https://pymotw.com/2/argparse/)
+ [python argparse](http://blog.csdn.net/zhanglingge/article/details/18009581)
