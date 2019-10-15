#! python3
class Folder():

    def __init__(self, name, subfolders=[], level=0, parent=None, type='directory'):
        self.name = name
        self.path = ''
        self.subfolders = subfolders
        self.level = level
        self.parent = parent
        self.type = type

    def addFolder(self, newfolder):
        self.subfolders.append(newfolder)

    def pathEvaluator(self):
        current = self
        path = ['dir']
        while current.name != 'dir':
            path.insert(1, current.name)
            if current.parent:
                current = current.parent
        self.path = '\\'.join(path)


class File(Folder):
    def __init__(self, name, subfolders=None, level=0, parent=None, type='file'):
        super().__init__(name, subfolders, level, parent, type)
        self.name = name


def folderLevelGenerator(dir):
    level = 0
    ptr = 0
    while dir[ptr:ptr+2] == '\\t':
        level += 1
        ptr += 2
    return level


def longestPath(tree_heap):
    # recursive function to be added here
    maximum_path_length = 0
    max_path_index = 0
    for index, dir in enumerate(tree_heap):
        if len(dir.path) > maximum_path_length and dir.type == 'File':
            maximum_path_length = len(dir.path)
            max_path_index = index
    return tree_heap[index].path


path = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
path = path.split('\\n')
folder_stack = []
ptr = 0
for dir in path:
    dir_level = folderLevelGenerator(dir)
    dir_name = dir[dir_level*2::]
    if '.' in dir_name:
        folder_stack.append(File(name=dir_name, level=dir_level))
    else:
        folder_stack.append(Folder(name=dir_name, level=dir_level))
    ptr += 1
parent = folder_stack[0]
tree_heap = [parent]
del folder_stack[0]
for index, folder in enumerate(folder_stack):
    parent_level = folder.level - 1
    ptr = len(tree_heap) - 1
    while folder.parent == None and ptr >= 0:
        if tree_heap[ptr].level == parent_level:
            folder_stack[index].parent = tree_heap[ptr]
            folder_stack[index].pathEvaluator()
            tree_heap[ptr].addFolder(folder)
            tree_heap.append(folder)
            break
        ptr -= 1
print(longestPath(tree_heap))
