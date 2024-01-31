---
marp: true
theme: uncover
class: invert
---

# Stable Diffusion

## Down the Rabbit Hole

Jan Mayer, 02.02.2024

---

### Example: Fooocus

`hummingbird sipping nectar from a flower`

---

## Stable Diffusion?

> Stable Diffusion is a [deep learning](), [text-to-image]() model released in 2022 based on [diffusion](https://en.wikipedia.org/wiki/Diffusion_model) techniques.

https://en.wikipedia.org/wiki/Stable_Diffusion

---

## Diffusion?

> ... involves training a neural network to sequentially [denoise]() images blurred with [Gaussian noise](). The model is trained to reverse the process of adding noise to an image.

https://en.wikipedia.org/wiki/Diffusion_model

<!--
Diffusion models are taught to remove noise from an image.
-->

---

## Learning Process

- Data Preparation: Images encoded into [latent space]()
- Forward Diffusion (Noising):
  - Gradual addition of noise over a series of steps
  - Transforms the original into completely noisy state
- Model learns to reverse the diffusion process

---

## Generation

- Begin with a **random noise input**
- Reverse Diffusion (Denoising):
  - **Iteratively** applies the learned reverse process to the initial noise
  - At each step, the model predicts and subtracts the added noise, gradually denoising the data.
- **conditioned** on text descriptions
- (plus additional magic)

Note: Deterministic with same settings + seed!

---

- **Model**:
  - trained neural network saved to disk
  - `.safetensor`, ~6 GB
  - Base Models: SD 1.5, SDXL 1.0
  - Merges of the Base Models and further training
- **Lora** (Low-Rank Adaptation):
  - technique for fine-tuning the model
  - effective addition of specific concepts
  - `.safetensor`, ~100 MB
  - often react to specific keywords

---

## Example: Fooocus Advanced

[Juggernaut XL v8](https://civitai.com/models/133005?modelVersionId=288982) + [Bricks Style Lora](https://civitai.com/models/274576/bricks-style-sdxl) + [Fried Egg Style Lora](https://civitai.com/models/255828/fried-egg-style-lora-15sdxl)

`ais-brickz hummingbird sipping nectar from a ral-friedegg flower`

---

Python
Torch with CUDA

---

## civitai.com

- Models
- Loras
- Images for Inspiration
- ...

---

## Example: A11111

(Read: automatic eleven eleven)

---

## Prompting

- Loads of wrong, old, or contradicting information
  - e.g.: big blocks of negative prompts - cargo cult from years ago
  - photorealism does not mean what you want, use `photo`
- Use Braces for emphasis (man) (handsome:1.5)

---

- Scheduler: A mechanism that controls the rate and pattern at which noise is added or removed during the diffusion process. (Normal, [Karras](https://arxiv.org/abs/2206.00364))
- Sampler: A sampling method used during the generation process to better refine and select the image outputs based on certain criteria or conditions. (Euler, DPM++ 2M)

---

## Example: ComfyUI

---

- CLIP: A model used for text-to-image tasks, guiding the image generation in Stable Diffusion to align with textual descriptions.
- VAE (Variational Autoencoder): Used in the initial stages of Stable Diffusion to encode images into a latent space, from which the diffusion process begins.

---

## Example: ComfyUI Advanced Workflows

- FaceDetailer
- Upscaler
- Control Net
    - IP Adapter
    - IP Adapter Face ID
- ...

---

## GUIs

- Fooocus: Just works - easy results. SDXL only.
- A1111: Most tutorials reference this, many plugins.
- ComfyUI: Learning Cliff, in-detail configuration
- SD.Next / Vlad / Easy Diffusion: A1111, but sucks less
- Invoke AI: Mix of A1111 and ComfyUI

---

## Notes on GUIs

- All Python + Webserver
- Main UI + Plugins
  - Random Python Repos
  - Downloads even more repos
  - Auto updates, auto pip installs
  - Downloads GB of stuff

-> Security Nightmare

stable-diffusion-webui-docker exists, but does not work that well with Plugins

---

## Run locally

- GTX 1060 6 GB:
  - SD 1.5: ~20 sec/image
  - complex SDXL 1.0 workflow: 5+ min/image
- VRAM >> everything else
- GTX 4090 24 GB is the best consumer card ~1900€
- other Nvidia Cards 16GB [450€+](https://geizhals.de/?cat=gra16_512&xf=10825_04+-+GeForce+RTX%7E132_16384)
- it *does* work with AMD, but don't

---

## Run in the Cloud

- Google Colab (got kicked on free tier)
- rundiffusion.com ~0.50$/h
- runpod.io / vast.ai
- ...

but then its running in the cloud ...

---

## My Takeways

- Not easy, but a lot of fun
  - Many duds / fails, many reruns required
  - Worse than Midjourney, but Control is great
  - Problems: Lack of Imagination + PC 💩
- SD 1.5 base model sucks
  - derivative models okay-ish
  - +Loras, +ADetailer, +HiRes Fix
- SDXL much better - and much slower
- Continue with ComfyUI

---

## Further Reading

Note: A lot of information is out of date or just wrong.

- https://civitai.com/
- https://www.reddit.com/r/StableDiffusion/
- https://en.wikipedia.org/wiki/Stable_Diffusion
- https://en.wikipedia.org/wiki/Diffusion_model
- https://medium.com/sogetiblogsnl/an-introduction-to-stable-diffusion-efd5da6b3aeb
- https://www.youtube.com/watch?v=1CIpzeNxIhU
- https://staffordwilliams.com/blog/2023/05/19/introduction-to-stable-diffusion/
