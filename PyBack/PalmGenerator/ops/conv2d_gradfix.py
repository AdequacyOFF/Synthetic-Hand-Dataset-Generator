"""Custom replacement for `torch.nn.functional.conv2d` that supports
arbitrarily high order gradients with zero performance penalty."""

import contextlib
import torch

#----------------------------------------------------------------------------

weight_gradients_disabled = False   # Forcefully disable computation of gradients with respect to the weights.

@contextlib.contextmanager
def no_weight_gradients():
    global weight_gradients_disabled
    old = weight_gradients_disabled
    weight_gradients_disabled = True
    yield
    weight_gradients_disabled = old

#----------------------------------------------------------------------------

def conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1):
    return torch.nn.functional.conv2d(input=input, weight=weight, bias=bias, stride=stride, padding=padding, dilation=dilation, groups=groups)

def conv_transpose2d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1):
    return torch.nn.functional.conv_transpose2d(input=input, weight=weight, bias=bias, stride=stride, padding=padding, output_padding=output_padding, groups=groups, dilation=dilation)

#----------------------------------------------------------------------------
