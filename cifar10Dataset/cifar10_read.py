# -*- coding: utf-8 -*-
import cPickle

def unpickle(file):
    with open(file,'rb') as fo:
        dict = cPickle.load(fo)
    return dict
    
    
if __name__ == '__main__':
    print (unpickle('./Users/pengl/Documents/PythonSpyderTest/cifar10Dataset/data_batch_0'))
