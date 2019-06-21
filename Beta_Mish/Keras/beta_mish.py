# -*- coding: utf-8 -*-
"""Function Definition of Beta_Mish in Keras
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras.engine.base_layer import Layer
from keras import backend as K

class beta_mish(Layer):
    """Beta Mish Activation Function.
    It follows:
    `f(x) = x * tanh(ln((1 + exp(x))^\\beta))`.
    # Input shape
        Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
    # Output shape
        Same shape as the input.
    # Arguments
        beta: A constant or a trainable parameter (default = 1.5)
    # References
        - [β-Mish: An uni-parametric adaptive activation function derived from Mish.](
           https://github.com/digantamisra98/Beta-Mish)
    """

    def __init__(self, beta=1.5, **kwargs):
        super(beta_mish, self).__init__(**kwargs)
        self.supports_masking = True
        self.beta = K.cast_to_floatx(beta)

    def call(self, inputs):
        return inputs*K.tanh(K.log(K.pow((1+K.exp(inputs)),self.beta)))

    def get_config(self):
        config = {'beta': float(self.beta)}
        base_config = super(beta_mish, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def compute_output_shape(self, input_shape):
        return input_shape
