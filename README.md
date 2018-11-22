# GRE3000 Excel Version

## Words-learning Script

The word lists are located in `./wordcsv` from 1 to 16. Run python script to learn those: `$ python learning.py <list_number>`

For `List 1`

    python learning.py 1

![learning-demo](https://raw.githubusercontent.com/HaoPeiwen/GRE3000Excel/master/demo.png)

You can use `<KeyPress>`: 

- `Left`: Previous
- `Down`: Forget
- `Right`: Rememebr
- `Up`: Search (Using [Wudao command dict](#1.3))


## Tkinter (for Python 3.x)

**Note**: Check the version, Python 3.x only

If you are on Ubuntu, you probably need to run [update-python-modules](http://manpages.ubuntu.com/manpages/trusty/en/man8/update-python-modules.8.html) to update your Tkinter module for Python 3.

First, make sure you have `python-support` installed:

    sudo apt-get install python-support
Then, run `update-python-modules` with the `-a` option to rebuild all the modules:

    sudo update-python-modules -a

## Wudao Dict - Command dictionary

![py](https://img.shields.io/badge/python-3.4.5-green.svg?style=plastic)![plat](https://img.shields.io/badge/platform-Ubuntu/CentOS/Debian-green.svg?style=plastic)

Forked from [ChestnutHeng/Wudao-dict](https://github.com/ChestnutHeng/Wudao-dict).


![Zh_En Demo](https://raw.githubusercontent.com/HaoPeiwen/GRE3000Excel/master/wudao.png)

## Usage

    wd <word_en or word_zh>

To see help:

    $ wd -h
    Usage: wd [OPTION]... [WORD]
    Youdao is wudao, a powerful dict.
    -k, --kill             kill the server process    (退出服务进程)
    -h, --help             display this help and exit (查看帮助)
    -s, --short-desc       do not show sentence       (只看释义)
    -n, --not-save         query and save to notebook (不存入生词本)
    生词本文件: ... some path .../notebook.txt
    查询次数: ... some path .../usr_word.json
