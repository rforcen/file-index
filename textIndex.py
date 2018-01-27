import re
from collections import OrderedDict, Counter


def _fileIndex(fh):
    ''' create a dict using Counter of a
    flat list of words (re.findall(re.compile(r"[a-zA-Z]+"), lines)) in (lines in file->for lines in fh)
    '''
    return Counter(
        [wrd.lower() for wrdList in
         [words for words in
          [re.findall(re.compile(r'[a-zA-Z]+'), lines) for lines in fh]]
         for wrd in wrdList])


def fileIndex(fnme):
    ' create a dict (word:count) from text file'
    with open(fnme, 'r') as fh:
        return _fileIndex(fh)


def _sort_by_key_count(d, index):  # 0=key, 1=count
    sb = OrderedDict(sorted(d.items(), key=lambda t: t[index], reverse=index == 1))
    return [i for i in sb.items()]


def sortbyKey(d):
    return _sort_by_key_count(d, 0)


def sortbyCount(d):
    return _sort_by_key_count(d, 1)


if __name__ == '__main__':
    d = fileIndex('bible.txt')

    print(sortbyKey(d))
    print(sortbyCount(d))
