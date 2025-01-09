= Homework 1: Hodgkin-Huxley(HH) model
陈启钰 物理学院 2300011447

选择ENa为调节的参数，通过选取不同的参数值，画出HH模型的动作电位图如下。

#figure(
  image("ENa=10.svg",width: 70%),
  caption: [ENa = 10mV],  
)
#figure(
  image("ENa=20.svg",width: 70%),
  caption: [ENa = 20mV],  
)
#figure(
  image("ENa=30.svg",width: 70%),
  caption: [ENa = 30mV],  
)
#figure(
  image("ENa=40.svg",width: 70%),
  caption: [ENa = 40mV],  
)
#figure(
  image("ENa=50.svg",width: 70%),
  caption: [ENa = 50mV],  
)
#figure(
  image("ENa=60.svg",width: 70%),
  caption: [ENa = 60mV],  
)
#figure(
  image("ENa=70.svg",width: 70%),
  caption: [ENa = 70mV],  
)
#figure(
  image("ENa=80.svg",width: 70%),
  caption: [ENa = 80mV],  
)
#figure(
  image("ENa=90.svg",width: 70%),
  caption: [ENa = 90mV],  
)
#figure(
  image("ENa=100.svg",width: 70%),
  caption: [ENa = 100mV],  
)
几个规律：
- 由十幅图的对比可以很明显的看出，随着ENa的增大，动作电位的幅值增大，峰变得更加尖锐。

- 同时还发现，在ENa从50mV到60mV的时候，绿色的线被“激发”，也就是绿线所对应的输入达到了阈值从而激发了动作电位，而橙线、蓝线始终没有被激发

- 动作电位的幅值几乎与输入无关（几个峰几乎等高）