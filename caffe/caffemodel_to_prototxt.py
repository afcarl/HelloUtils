#coding=utf-8
'''
@author: kangkai
'''
# https://www.zhihu.com/question/59597255/answer/168686857

import sys
sys.path.append('E:\Git\caffe_cuhk\python')

from caffe.proto import caffe_pb2

def toPrototxt(modelName, deployName):
    with open(modelName, 'rb') as f:
        caffemodel = caffe_pb2.NetParameter()
        caffemodel.ParseFromString(f.read())
        
    # 兼容新旧版本
    # LayerParameter 消息中的 blobs 保存着可训练的参数
    
    for item in caffemodel.layers:
        item.ClearField('blobs')
    for item in caffemodel.layer:
        item.ClearField('blobs')
        
    # print(caffemodel)
    with open(deployName, 'w') as f:
        f.write(str(caffemodel))
        
if __name__ == '__main__':
    #modelName = 'facenet_iter_14000.caffemodel'
    #deployName = 'facenet_deploy.prototxt'
    
    # https://github.com/shicai/MobileNet-Caffe
    modelName = 'E:\Git\MobileNet-Caffe\mobilenet.caffemodel'
    deployName = 'E:\Git\MobileNet-Caffe\mobilenet_deploy_test.prototxt'
    toPrototxt(modelName, deployName)