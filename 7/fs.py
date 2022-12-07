from typing import List


class Dir:

    def __init__(self, name, parent=None):
        self.name = name
        self.dirs: List[Dir] = []
        self.files: List[File] = []
        self.parent: Dir = parent

    def _get_dir(self, name):
        for d in self.dirs:
            if name == d.name:
                return d

    def _get_file(self, name):
        for f in self.files:
            if name == f.name:
                return f

    def add_dir(self, d):
        d.parent = self
        if self._get_dir(d.name) is None:
            self.dirs.append(d)

    def add_file(self, f):
        f.parent = self
        if self._get_file(f.name) is None:
            self.files.append(f)

    def cd(self, arg):
        if arg == '/':
            d = self.parent or self
            while d.parent is not None:
                d = d.parent
        elif arg == '..':
            d = self.parent
        else:
            d = self._get_dir(arg) or Dir(arg, parent=self)
        return d

    def sizeof(self):
        files = sum(f.size for f in self.files)
        dirs = sum(d.sizeof() for d in self.dirs)
        return files + dirs

    def walk(self):
        yield self
        for d in self.dirs:
            yield from d.walk()

    def print(self, depth=0, indent=2):
        print(f"{' '*depth*indent} - {self.name}")
        for d in self.dirs:
            print(f"{' '*(depth+1)*indent} - {d.name} (dir)")
            for f in d.files:
                print(f"{' '*(depth+2)*indent} - {f.name} ({f.size})")
            for sub in d.walk():
                sub.print(depth=depth+1)
        for f in self.files:
            print(f"{' '*depth*indent} - {f.name} ({f.size})")


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
        self.parent = None


def parse(data):
    d = Dir(name='/')
    for line in data:
        parts = line.split(' ')
        if parts[0].startswith('$'):
            parts = line.split(' ')
            cmd = parts[1]
            if cmd == 'cd':
                d = d.cd(parts[2])
            if cmd == 'ls':
                continue
        elif parts[0].startswith('dir'):
            d.add_dir(Dir(parts[1]))
        else:
            d.add_file(File(parts[1], parts[0]))

    return d.cd('/')


def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f.readlines()]
    root = parse(data)
    root.print()

    # part 1
    total = 0
    for d in root.walk():
        if (s := d.sizeof()) <= 100000:
            total += s
    print(f"total of dirs <= 100000: {total}")

    # part 2
    min_size = 30000000 - (70000000 - root.sizeof())
    delete = root
    for d in root.walk():
        if (s := d.sizeof()) >= min_size:
            print(d.name, s)
            if s < delete.sizeof():
                delete = d
    print(f"Smallest directory to be deleted: {delete.name} ({delete.sizeof()})")


if __name__ == '__main__':
    main()
