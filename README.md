<p align="center">
  <img width="300" src="Observations/logo_transparent.png">
</p>

# β-Mish

<div style="text-align:center"><img src ="Observations/function.png"  width="400"/></div>
<div style="text-align:center"><img src ="Observations/Mish3.png"  width="800"/></div>
<div style="text-align:center"><img src ="Observations/Derivatives.png"  width="800"/></div>

## Results

### CIFAR-10:

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
