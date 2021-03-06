<p align="center">
  <img width="300" src="Observations/logo_transparent.png">
</p>

[![HitCount](http://hits.dwyl.io/digantamisra98/Beta-Mish.svg)](http://hits.dwyl.io/digantamisra98/Beta-Mish)
[![Donate](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/digantamisra98/Beta-Mish/issues)

# 🧠 β-Mish

β-Mish is an uni-parametric activation activation inspired from Mish activation function. When β=1, β-Mish becomes the standard version of Mish. 
β-Mish can be mathematically represented using the function: 
<div style="text-align:center"><img src ="Observations/func.png"  width="280"/></div>
The partial derivatives of the function are:
<div style="text-align:center"><img src ="Observations/partial_x.png"  width="520"/></div>
<div style="text-align:center"><img src ="Observations/partial_beta.png"  width="300"/></div>
When β=1.5, the function has the following 1<sup>st</sup> derivative:
<div style="text-align:center"><img src ="Observations/dev.png"  width="340"/></div>

If β=1.5, the function ranges from: ≈-0.451103 to ∞. For most benchmarks, β was set to be 1.5.
<div style="text-align:center"><img src ="Observations/Mish3.png"  width="800"/></div>
<div style="text-align:center"><img src ="Observations/Derivatives.png"  width="800"/></div>
<div style="text-align:center"><img src ="Observations/All.png"  width="1000"/></div>
<div style="text-align:center"><img src ="Observations/Contour.png"  width="600"/></div>

## Results

### MNIST:

#### LeNet-4:

| Activation Function  | Accuracy (20*) |  Loss (20*) | GPU-Utilization (20*) |CPU-RAM Utilization** (20*)| Training Time (20*) | Inference Time (20*)| Top 5 Accuracy (20*) | Top 3 Accuracy (20*)|
| ------------- | ------------- | ---|---|---|---|---|---|---|
| ReLU  | **98.65%**  |**0.368%**|5%|**11.4GB**|**51.67 seconds**|**0.197 seconds**|**100%**|99.94%|
| Swish-1  | 98.42%  |0.385%|5%|**11.4GB**|65.11 seconds|0.2157 seconds|99.99%|99.9%|
| Mish  | 98.64%  |**0.368%**|5%|11.2GB|81.12 seconds|0.2967 seconds|**100%**|99.94%|
|β-Mish (β=1.5)|98.45%|0.4648%|5%|10.9GB|84.87 seconds|0.3061 seconds|**100%**|**99.97%**|

<em> *The number indicates the Number of Epochs
</em><br>
<em> **This shows the amount of RAM Free.
</em><br>

### Fashion-MNIST:

#### Mini VGG:

| Activation Function  | Accuracy (25*) |  Loss (25*) | 
| ------------- | ------------- | ---|
| ReLU  | 93.19%  |1.895%|
| Swish-1  | 93.09%  |1.935%|
| Mish  | 93.31%|1.859%|
|β-Mish (β=1.5)|**93.44%**|**1.8222%**|

<em> *The number indicates the Number of Epochs
</em><br>

### CIFAR-10:

#### ResNet v1:

##### ResNet-20:

|Activation Function| Top-1 Accuracy| Loss|
|---|---|---|
|Mish|91.81%|4.47284%|
|Swish-1|**91.95%**|**4.440651%**|
|ReLU|91.5%|4.94356%|
|β-Mish (β = 1.5)|91.75%|4.4894%|

##### ResNet-32:

|Activation Function| Top-1 Accuracy| Loss|
|---|---|---|
|Mish|92.29%|4.3543639%|
|Swish-1|92.3%|**4.31110565%**|
|ReLU|91.78%|4.51267568%|
|β-Mish (β = 1.5)|**92.49%**|4.49838%|

#### ResNet v2:

##### ResNet-20:

|Activation Function|Testing Top-1 Accuracy|Testing Loss|
|---|---|---|
|Aria-2(β = 1, α=1.5)|91.73%|4.25074%|
|Bent's Identity|89.1%|4.52398%|
|ELU(α=1.0)|91.58%|**4.05194%**|
|Hard Sigmoid|87.42%|4.86469%|
|Leaky ReLU(α=0.3)|90.57%|4.093131%|
|Mish|92.02%|4.19176%|
|PReLU(Default Parameters)|91.25%|4.403224%|
|ReLU|91.71%|4.08291%|
|SELU|90.59%|4.36311%|
|Sigmoid|89.27%|4.474636%|
|SoftPlus|91.39%|4.2238%|
|SoftSign|90.45%|4.402751%|
|Swish-1|91.61%|4.295542%|
|TanH|90.99%|4.3992%|
|Thresholded ReLU(θ=1.0)|76.22%|7.37498%|
|β-Mish (β=1.5)|**92.15%**|4.18306%|

#### Inception-ResNet v2:

|Activation Function |Testing Top-1 Accuracy|Testing Top-3 Accuracy|Testing Top-5 Accuracy|Testing Loss|
|---|---|---|---|---|
|Mish|**85.21%**|97.13%|99.22%|4.6409%|
|Swish-1|84.96%|97.29%|99.29%|4.8955%|
|ELU(α=1.0)|83.93%|96.96%|99.11%|4.884%|
|ReLU|82.22%|95.87%|98.65%|5.3729%|
|Leaky ReLU(α=0.3)|84.67%|**97.35%**|**99.42%**|**4.5577%**|
|TanH|76.29%|94.65%|98.42%|6.7464%|
|PReLU(Default Parameters)|81.99%|96.01%|99.04%|5.50853%|
|SELU|83.27%|96.61%|99.04%|5.1101%|
|Softsign|79.76%|95.15%|98.61%|6.0377%|
|β-Mish (β=1.5)|84.83%|97.19%|99.35%|4.8412%|

#### Capsule Network:

|Activation Function |Testing Top-1 Accuracy|Testing Top-3 Accuracy|Testing Top-5 Accuracy|Testing Loss (Margin Loss)|
|---|---|---|---|---|
|ELU(α=1.0)|71.7%|90.72%|95.85%|2.3819%|
|Mish|83.15%|94.62%|97.2%|1.51671%|
|Swish-1|82.48%|94.7%|97.11%|1.5232%|
|ReLU|82.19%|94.88%|97.48%|1.51009%|
|SELU|80.24%|94.3%|97.56%|1.9122%|
|Leaky ReLU(α=0.3)|**83.42%**|**95.48%**|**97.96%**|1.5393%|
|β Mish (β=1.5)|83.15%|94.98%|97.5%|**1.4803%**|

### Caravan Image Masking Challenge Dataset:
 
#### U-Net:

| Activation Function  | Training Loss (5*) |  Training Dice-Loss (5*) | Validation Loss(5*)| Validation Dice-Loss(5*)| Average Epoch Time | Average Step Time|
| ------------- | ------------- | ---|---|---|---|---|
| ReLU  |  0.724% |0.119%|0.578%|0.096%|**343.2 seconds**|**253 milli-seconds**|
| Swish-1  | 0.665%|0.111%|0.639%|0.108%|379 seconds|279.2 milli-seconds|
| Mish  |0.574%|**0.097%**|0.554%|**0.092%**|411.2 seconds|303 milli-seconds|
|β Mish (β=1.5)|**0.296%**|0.144%|**0.228%**|0.121%|647 seconds|476.6 milli-seconds|

<em> *The number indicates the Number of Epochs
</em><br>
