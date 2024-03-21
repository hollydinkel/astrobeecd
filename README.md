# Multi-Agent 3D Map Reconstruction and Change Detection in Microgravity with Free-Flying Robots

<p>
  <a href="https://github.com/hollydinkel/astrobee_change_detection/actions/workflows/build.yml?query=branch%3Amaster" alt="GitHub Actions">
    <img src="https://img.shields.io/github/actions/workflow/status/hollydinkel/astrobee_change_detection/build.yml?branch=master">
  </a>
</p>


This repository contains the FastCD Robot Operating System (ROS) package. It also contains helper scripts for converting Astrobee robot data into a format FastCD expects. The FastCD ROS package is applied to these Astrobee data, collected in space on the International Space Station and on earth in the NASA Ames Research Center Granite Lab, as documented in our paper *Multi-Agent 3D Map Reconstruction and Change Detection in Microgravity with Free-Flying Robots*, by Holly Dinkel*, Julia Di*, Jamie Santos, Keenan Albee, Paulo Borges, Marina Moreira, Ryan Soussan, Oleg Alexandrov, Brian Coltin, and Trey Smith.

*Denotes equal contribution.

<p align="center">
  <img src="images/inconsistency.png" width="2000" title="change_detection">
</p>

## Preparing Data From Astrobee

Follow the [data processing instructions](https://github.com/hollydinkel/astrobee_change_detection/blob/master/docs/data_processing.md).

## Using Prepared Data

Follow the [using FastCD instructions](https://github.com/hollydinkel/astrobee_change_detection/blob/master/docs/using_fastcd.md).

## Learn More

The [supplementary video](https://www.youtube.com/watch?v=VfjV-zwFEtU) describes the Astrobee platform, the change detection framework, and visualizes results.

[![supplementary video](https://img.youtube.com/vi/VfjV-zwFEtU/0.jpg)](https://www.youtube.com/watch?v=VfjV-zwFEtU)

## BibTex

```bash
@ARTICLE{
  dinkel2023astrobee,
  author={Dinkel, Holly and Di, Julia and Santos, Jamie and Albee, Keenan and Borges, Paulo and Moreira, Marina and Soussan, Ryan and Alexandrov, Oleg and Coltin, Brian and Smith, Trey},
  journal={Under Review}, 
  title={Multi-Agent 3D Map Reconstruction and Change Detection in Microgravity with Free-Flying Robots}, 
  year={2024}
}
```

## **References**
<a id="1">[1]</a> 
NASA, "Astrobee Robot Software," (2023). [[code]](https://github.com/nasa/astrobee)

<a id="3">[3]</a> 
E. Palazzolo and C. Stachniss, "Fast Image-Based Geometric Change Detection Given a 3D Model," in IEEE Int. Conf. Robot. Autom. (ICRA), 2018, pp. 6308–6315. doi: 10.1109/ICRA.2018.
8461019 [[paper]](https://ieeexplore.ieee.org/document/8461019) [[code]](https://github.com/PRBonn/fast_change_detection)