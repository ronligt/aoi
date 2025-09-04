# Single molecule based super-resolution microscopy

Single-molecule based super-resolution methods are a family of superresolution microscopy techniques that achieve sub-diffraction resolution by imaging independent and stochastically blinking fluorophores over time. The gain in spatial resolution is traded with temporal resolution as the acquisition of many camera frames is required to computationally reconstruct a single super-resolved image. Typically, conventional widefield microscopes are combined with (photo)activatable or switchable fluorescent probes, but more advanced camera-based as well as scanning image acquisition have also been successful.

The most common use of stochastic switching is applied in a family of techniques known as single-molecule localization microscopy (SMLM). SMLM exploits the temporal separation of spatially overlapping fluorophores in an image series to determine the position of single nolecules with nanometer localization precision numerically. Temporal separation is accomplished by switching on only a small fraction (<1\%) of molecules located in a field of view. The single reconstructed image consists of the localizations of many thousands of molecules. The implementations mainly differ in the mechanisms that are exploited to achieve the necessary sparse blinking.

More recently, a range of alternative techniques were developed that do not require isolating single-molecules for position determination. They can analyze fluctuations in fluorescence emission over time and tolerate a wider range of switching behaviour and imaging conditions. One of the most researched is super-resolution optical fluctuation imaging (SOFI), and others include e.g SRRF, SPARCOM and 3B. A common feature of fluctuation-based techniques is that they require less input frames and lower laser powers as SMLM, making them more live-cell compatible at the cost of a reduced gain in resolution.   

```{note}
If you want to read up more about SMLM and fluctuation-based methods, I recommend the following reviews:
* Lelek, M., Gyparaki, M.T., Beliu, G. et al. Single-molecule localization microscopy. Nat Rev Methods Primers 1, 39 (2021). 
* Monika Pawlowska
et al, Embracing the uncertainty: the evolution of SOFI
into a diverse family of fluctuation-based super-
resolution microscopy methods, 2022
J. Phys. Photonics 4 012002

This chapter on SMLM partially follows M. Fazel, K. S. Grussmayer, B. Ferdman, A. Radenovic, Y. Shechtman, J. Enderlein, S. Pressé, Fluorescence Microscopy: a statistics-optics perspective, [OA, arXiv:2304.01456].
```
## Single molecule localization microscopy (SMLM) algorithm

## SMLM - blinking mechanisms

## 3D SMLM

## SMLM quality 


