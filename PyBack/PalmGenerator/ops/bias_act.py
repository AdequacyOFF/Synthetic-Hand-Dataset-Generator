import torch
import dnnlib

activation_funcs = {
    'linear':   dnnlib.EasyDict(func=lambda x, **_:         x,                                          def_alpha=0,    def_gain=1,             cuda_idx=1, ref='',  has_2nd_grad=False),
    'relu':     dnnlib.EasyDict(func=lambda x, **_:         torch.nn.functional.relu(x),                def_alpha=0,    def_gain=torch.sqrt(torch.tensor(2)),    cuda_idx=2, ref='y', has_2nd_grad=False),
    'lrelu':    dnnlib.EasyDict(func=lambda x, alpha, **_:  torch.nn.functional.leaky_relu(x, alpha),   def_alpha=0.2,  def_gain=torch.sqrt(torch.tensor(2)),    cuda_idx=3, ref='y', has_2nd_grad=False),
    'tanh':     dnnlib.EasyDict(func=lambda x, **_:         torch.tanh(x),                              def_alpha=0,    def_gain=1,             cuda_idx=4, ref='y', has_2nd_grad=True),
    'sigmoid':  dnnlib.EasyDict(func=lambda x, **_:         torch.sigmoid(x),                           def_alpha=0,    def_gain=1,             cuda_idx=5, ref='y', has_2nd_grad=True),
    'elu':      dnnlib.EasyDict(func=lambda x, **_:         torch.nn.functional.elu(x),                 def_alpha=0,    def_gain=1,             cuda_idx=6, ref='y', has_2nd_grad=True),
    'selu':     dnnlib.EasyDict(func=lambda x, **_:         torch.nn.functional.selu(x),                def_alpha=0,    def_gain=1,             cuda_idx=7, ref='y', has_2nd_grad=True),
    'softplus': dnnlib.EasyDict(func=lambda x, **_:         torch.nn.functional.softplus(x),            def_alpha=0,    def_gain=1,             cuda_idx=8, ref='y', has_2nd_grad=True),
    'swish':    dnnlib.EasyDict(func=lambda x, **_:         torch.sigmoid(x) * x,                       def_alpha=0,    def_gain=torch.sqrt(torch.tensor(2)),    cuda_idx=9, ref='x', has_2nd_grad=True),
}

def bias_act(x, b=None, dim=1, act='linear', alpha=None, gain=None, clamp=None):
    assert act in activation_funcs
    spec = activation_funcs[act]
    alpha = spec.def_alpha if alpha is None else alpha
    gain = spec.def_gain if gain is None else gain
    
    # Remove the clamp logic since it's not defined in the spec
    # clamp = max(clamp, spec.def_clamp) if clamp is not None else spec.def_clamp

    # Add bias.
    if b is not None:
        assert b.ndim == 1
        assert b.shape[0] == x.shape[dim]
        x = x + b.reshape([-1 if i == dim else 1 for i in range(x.ndim)])

    # Evaluate activation function.
    x = spec.func(x, alpha=alpha)

    # Scale by gain.
    if gain != 1:
        x = x * gain

    # Clamp if specified.
    if clamp is not None:
        x = x.clamp(-clamp, clamp)
    return x