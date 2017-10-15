# coding: utf-8

import numpy as np

if __name__ == '__main__':
    
    ma = np.matrix([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

    ### 检查矩阵
    print 'check_tpye: ' + type(ma).__name__
    print 'check_ma_data:'
    print ma
    
    ### 矩阵乘法: matrix multiplication
    ma_ma_product = ma * ma
    print ma_ma_product

    ma_ma_product = np.dot(ma, ma)
    '\n'
    print ma_ma_product

    mb = np.matrix([[11, 12], [21, 22], [31, 32]])
    mc = np.matrix([[11, 12, 13, 14], [21, 22, 23, 24]])
    
    ma_mb_mc_product = ma * mb * mc
    print '\nma_mb_mc_product :'
    print ma_mb_mc_product

    ### 矩阵转置: transpos
    ma_T = ma.transpose()
    print ma_T

    ### 矩阵的逆
    '''
    maa = ma ** (-1)
    maa = ma.I

    print 'matrix_a :'
    print maa
    '''
