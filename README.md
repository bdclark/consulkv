# consulkv

Simple command-line utility to set/delete/compare Consul key/values across
multiple consul servers (e.g. in multiple environments).

### Installation & Usage

```
pip install https://github.com/bdclark/consulkv/archive/master.zip
```

Create `~/consulkv.yml` (see sample in this repo).

```
$ consulkv --help
usage: consulkv [-h] [--config-file PATH]
                {show,backup,restore,ls,set,rm,sync} ...

positional arguments:
  {show,backup,restore,ls,set,rm,sync}
    show                Show Consul K/V store(s)
    backup              Backup Consul KV store(s)
    restore             Restore Consul KV store(s)
    ls                  List Consul keys
    set                 Set a Consul key
    rm                  Delete a Consul key
    sync                Sync a Consul key between environments

optional arguments:
  -h, --help            show this help message and exit
  --config-file PATH    config file path (default is $HOME/consulkv.yml)
```

Example of `show` command:
```
$ consulkv show --help
usage: consulkv show [-h] [--prefix PREFIX] [--suffix SUFFIX]
                     [--contains CONTAINS] [--out-of-sync]
                     [--env ENV [ENV ...]]

optional arguments:
  -h, --help           show this help message and exit
  --prefix PREFIX      key prefix to filter by
  --suffix SUFFIX      key suffix to filter by
  --contains CONTAINS  only include keys containing a string
  --out-of-sync        only show keys where backup out-of-sync with API
  --env ENV [ENV ...]  environments to include
```

### License
```
MIT License

Copyright (c) 2016 Brian clark <brian@clark.zone>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
