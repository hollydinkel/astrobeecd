# AstrobeeCD: Change Detection in Microgravity with Free-Flying Robots
**Published in Acta Astronautica ([ScienceDirect](https://doi.org/10.1016/j.actaastro.2024.06.037))**

<p>
  <a href="https://github.com/hollydinkel/astrobeecd/actions/workflows/build.yml?query=branch%3Amaster" alt="GitHub Actions">
    <img src="https://img.shields.io/github/actions/workflow/status/hollydinkel/astrobeecd/build.yml?branch=master">
  </a>
  <a href='https://arxiv.org/pdf/2311.02558'><img src='https://img.shields.io/badge/ArXiv-2311.02558-red'>
  </a> 
</p>

This repository contains the code for AstrobeeCD, a system for 3D scene change detection toward near-real-time environmental awareness of space outposts using the Astrobee free-flying robot in microgravity. A set of image and depth data from one time step is used to reconstruct a 3D model of the environment. The 3D model is used as the basis for comparison for free-flyer environment surveys at future time steps, where an image-based change detection algorithm identifies inconsistencies against the 3D model. Change detection is demonstrated using real image and pose data collected by an Astrobee robot in space on the International Space Station and on earth in the NASA Ames Research Center Granite Lab.

<p align="center">
  <img src="images/astrobee-iss.gif" width="500" title="Astrobee">
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
@ARTICLE{dinkel2024astrobeecd,
    author = {Dinkel, Holly and Di, Julia and Santos, Jamie and Albee, Keenan and Borges, Paulo V.K. and Gouveia Moreira, Marina and Soussan, Ryan and Alexandrov, Oleg and Coltin, Brian and Smith, Trey},
    title = {\href{https://doi.org/10.1016/j.actaastro.2024.06.037}{AstrobeeCD: Change Detection in Microgravity with Free-Flying Robots}},
    journal= {Acta Astronautica},
    volume = {223},
    pages = {98-107},
    year = {2024},
    issn = {0094-5765},
    doi = {https://doi.org/10.1016/j.actaastro.2024.06.037},
}
```

## **References**
<a id="1">[1]</a> 
NASA, "Astrobee Robot Software," (2023). [[code]](https://github.com/nasa/astrobee)

<a id="2">[2]</a> 
E. Palazzolo and C. Stachniss, "Fast Image-Based Geometric Change Detection Given a 3D Model," in IEEE Int. Conf. Robot. Autom. (ICRA), 2018, pp. 6308–6315. doi: 10.1109/ICRA.2018.
8461019 [[paper]](https://ieeexplore.ieee.org/document/8461019) [[code]](https://github.com/PRBonn/fast_change_detection)
