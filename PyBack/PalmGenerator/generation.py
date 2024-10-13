
from pytorch_pretrained_biggan import BigGAN, BigGANConfig, one_hot_from_int, truncated_noise_sample
import torch
from torchvision.utils import save_image
import numpy as np

def load_model(path_to_ckp, device='cpu'):
  conf = BigGANConfig()
  conf = conf.from_dict({'output_dim': 512,
                         'z_dim': 128,
                         'class_embed_dim': 128,
                         'channel_width': 128,
                         'num_classes': 1000,
                         'layers': [[False, 16, 16],
                                    [True, 16, 16],
                                    [False, 16, 16],
                                    [True, 16, 8],
                                    [False, 8, 8],
                                    [True, 8, 8],
                                    [False, 8, 8],
                                    [True, 8, 4],
                                    [False, 4, 4],
                                    [True, 4, 2],
                                    [False, 2, 2],
                                    [True, 2, 1],
                                    [False, 1, 1],
                                    [True, 1, 1]],
                         'attention_layer_position': 8,
                         'eps': 0.0001,
                         'n_stats': 51})
  
  generator = BigGAN(conf)
  generator.load_state_dict(torch.load(path_to_ckp))
  generator.eval().to(device)

  return generator

def get_latent_input(batch_size, label, device='cpu'):
    noise = truncated_noise_sample(truncation=0.2, batch_size=batch_size)
    noise = torch.tensor(noise).float().to(device)

    label_one_hot = one_hot_from_int(label, batch_size=batch_size)
    label_one_hot = torch.tensor(label_one_hot).float().to(device)

    return noise, label_one_hot

def generate(generator, label, device='cpu'):
    
    with torch.no_grad():
        # Sample random latent vector z
        noise, class_embeds = get_latent_input(1, np.full((1), label), device) 
        # Generate image
        generated_image = generator(noise, class_embeds, truncation=0.2)[0].detach().cpu().permute((1, 2, 0)).numpy()
        
        generated_image = (generated_image + 1) / 2

        return generated_image



