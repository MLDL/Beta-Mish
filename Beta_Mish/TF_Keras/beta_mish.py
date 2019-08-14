# -*- coding: utf-8 -*-
"""Layers that act as activation functions.
"""

# Import Necessary Modules
import tensorflow as tf
from tensorflow.keras.layers import Layer

class BetaMish(Layer):
    '''
    β mish activation function.
    .. math::
        \\beta mish(x) = x * tanh(ln((1 + e^{x})^{\\beta}))
    Shape:
        - Input: Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
        - Output: Same shape as the input.
    Arguments:
        - beta: A constant or a trainable parameter (default = 1.5)
    References
        - β-Mish: An uni-parametric adaptive activation function derived from Mish:
        https://github.com/digantamisra98/Beta-Mish)
    '''

    def __init__(self, beta):
        super(BetaMish, self).__init__()
        self.beta = beta
    
    def call(self, inputs):
        return inputs * tf.math.tanh(tf.math.log(tf.math.pow(1 + tf.math.exp(inputs), self.beta)))