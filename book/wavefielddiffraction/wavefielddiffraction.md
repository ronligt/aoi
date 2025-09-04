(ch:wavefielddiffraction)
# Wavefield diffraction
We have seen that both the angular spectrum and the diffraction integral of Eq. {eq}`rs3` yield the same results. While the angular spectrum can be solved using computer calculations light propagation problems are easier to calculate with pen and paper using the diffraction integral under certain approximations.

## Diffraction integral
The typical diffraction geometry is shown in {numref}`diffractiongeom` where the object field, with lateral coordinates ($x_o, y_o$) is propagated to a detected field at distance $z$, with lateral coordinates ($x_i, y_i$). We can calculate the field $U(x_i, y_i, z)$ at the detection plane based on some object field $U(x_o, y_o)$ at $z=0$ using the Rayleigh-Sommerfeld diffraction integral of Eq. {eq}`rs3`

$$
\begin{equation}
	U(x_i, y_i, z)=\frac{1}{i \lambda} \int_{-\infty}^{\infty} U(x_o, y_o) \frac{\exp[ik|\mathbf{r}_i- \mathbf{r}_o|]}{|\mathbf{r}_i- \mathbf{r}_o|} \text{cos}\theta \, \text{d}x_o \text{d}y_o \, ,
\end{equation}
$$(rsdiff)

with $|\mathbf{r}- \mathbf{r}'|=\sqrt{(x_i-x_o)^2 + (y_i-y_o)^2 + z^2}$ and the distance between object and image point. The factor $\cos \theta = \frac{z}{|\mathbf{r}_i- \mathbf{r}_o|}$, which is the cosine of the angle between the propagation axis and the line connect object and detection point. The Rayleigh-Sommerfeld diffraction integral is exact. However, to make it easier to calculate the diffraction integral and obtain simplified expressions in some limiting cases we we embark on a number of approximations of Eq. {eq}`rsdiff`. 

```{figure} diffractiongeom.png
---
height: 200px
name: diffractiongeom
---
Geometry for the wavefield diffraction calculations.
```
(paraxial)=
## Paraxial approximation
The diffraction integral shows that the propagated field is the sum of many spherical waves. So for one detection point ($x_i, y_i$) rays from different directions reach the detection point. Now the 
[Paraxial approximation](https://en.wikipedia.org/wiki/Paraxial_approximation) states that these directions are approximately in the same direction as the propagation axis. In Eq.{eq}`rsdiff` this means that   

$$
\begin{equation}
	\cos \theta = \frac{z}{|\mathbf{r}_i- \mathbf{r}_o|} \approx 1 \, .
\end{equation}
$$

In other words the lateral extension of both object and detection coordinates is relatively small compared to the propagation distance $z$. Using the same argument we can approximate 

$$
\begin{equation}
	\frac{1}{|\mathbf{r}_i- \mathbf{r}_o|} \approx \frac{1}{z} \, .
\end{equation}
$$

Note that in particular this approximation does not lead to a large error as $|\mathbf{r}_i- \mathbf{r}_o|^{-1}$ varies very gradually with ($x_o, y_o$) and therefore mainly changes the magnitude of the result but not the dependence on ($x_i, y_i$).

## Fresnel approximation
After applying the paraxial approximations the diffraction integral is in a simpler form. However, mainly the exponential with $|\mathbf{r}_i- \mathbf{r}_o|$ makes it difficult to calculate the integral analytically. For example, the exponential function cannot be factorized nor is is simple to calculate an integrand for even the most simple forms of $U(x_o, y_o)$. So we need to further simplify the exponent. 

We do this by applying the Fresnel approximation and hence calculate the [Fresnel diffraction](https://en.wikipedia.org/wiki/Fresnel_diffraction) pattern. Using the expansion 
$\sqrt{1+\varepsilon} \approx 1+\frac{1}{2}\varepsilon-\frac{1}{8}\varepsilon^2+...$ the value of $|\mathbf{r}_i- \mathbf{r}_o|$ can be written as a sum. The Fresnel approximation is now to keep only up to the second term of the expansion. Hence, 

$$
\begin{equation}
	r_{01} = z \sqrt{ 1 + \left(\frac{x_i-x_o}{z}\right)^2 + \left(\frac{y_i-y_o}{z}\right)^2 } \approx z \left[ 1 + \frac{1}{2}\left(\frac{x_i-x_o}{z}\right)^2 + \frac{1}{2}\left(\frac{y_i-y_o}{z}\right)^2\right] \, .
\end{equation}
$$

In that case the Fresnel diffraction integral becomes (convolution form) 

$$
	U(x_i, y_i, z) =  \frac{\text{e}^{ikz}}{i \lambda z} \int_{\Sigma} U(x_o, y_o) \exp \left\{i \frac{k}{2 z} \left[ (x_i - x_o)^2 + (y_i - y_o)^2\right] \right\} \text{d}x_o \text{d}y_o \,  ,
$$

which also can be written as (Fourier transform form)

$$
	U(x_i, y_i, z)=\frac{\text{e}^{ikz}}{i \lambda z} \text{e}^{i\frac{k}{2z}(x_i^2 + y_i^2)}\int_{\Sigma} U(x_o, y_o) \text{e}^{i\frac{k}{2z}(x_o^2 + y_o^2)} \exp \left\{- i \frac{k}{z} \left[ x_i x_o + y_i y_o  \right] \right\} \text{d}x_o \text{d}y_o \, .  
$$

The first form of the Fresnel diffraction shows that the detected field is a convolution of the input field with a complex-valued Gaussian function. The second form shows that the detected field is a Fourier transform of the object field multiplied with a exponential with a quadratic phase of the object coordinates. The exponential with a quadratic phase of the detector coordinates before the integral does not affect the intensity of the diffracted field (it vanishes when $I=U U^*$ is calculated). 

### Validity of the Fresnel approximation
The Fresnel approximation is only valid when the third term 

$$
\begin{equation}
	\frac{z}{8}\left[\frac{1}{z^2} (x_i-x_o)^2 + \frac{1}{z^2}(y_i-y_o)^2\right]^2
\end{equation}
$$

is negligible. But what means negligible? The diffraction integral is integrating over a periodic functions. Hence, the  third term is only negligible when it is a lot smaller than $2\pi$. When we write out $\frac{1}{8}\varepsilon^2 \ll 2 \pi$ we find that

$$
\begin{equation}
	\frac{1}{\lambda^4}[(x_i-x_o)^2 + (y_i-y_o)^2]^2 \ll 8 \frac{z^3}{\lambda^3} \, ,
\end{equation}
$$

which should hold for all ($x_o, y_o$) and ($x_i, y_i$). In general $z$ is a factor bigger than the typical aperture sizes and the Fresnel approximation is fulfilled. 

The Fresnel approximation amounts to an approximation of the true phase difference between object and detected points, which is a spherical function, with a parabolic phase profile as shown in {numref}`phasefront`. For points that are far off the optical axis the approximation is incorrect. Hence, the Fresnel approximation also requires that rays should be close to parallel to the optical axis, similar to the {ref}`paraxial`.

```{figure} phasefront.png
---
height: 200px
name: phasefront
---
Wavefront
```
(sec:fresneltransfer)=
### Fresnel transfer function
The convolution form of the Fresnel transform can be written as $U(x_i, y_i, z)=h(x_o, y_o) \otimes U(x_o,y_o,0)$ with a point spread function 

$$
\begin{equation}
	h(x, y) = \frac{\text{e}^{i k z}}{i \lambda z} \exp \left[ i\frac{ k }{2 z}\left(x^2 + y^2 \right) \right] \, .
\end{equation}
$$

By taking the 2D Fourier transform of the PSF we can obtain the transfer function $H(f_x, f_y)$ in the Fresnel approximation 

$$
\begin{equation}
	{\cal{F}}\{ h(x,y,z)\} = \exp[i k z]\exp\left[ - i \pi \lambda z (f_x^2 + f_y^2) \right] \, . 
\end{equation}
$$

The first factor represents a phase that is identical for all angles and does not depend on ($f_x, f_y$). Hence, this first factor it does not influence the wavefield intensity. The second factor adds a quadratic phase to every spatial frequency. Considering the previously defined in section {ref}`sec:angularspectrum` the transfer function is

$$
\begin{equation}
	H(f_x, f_y, z) = \text{exp}\left[ i 2 \pi z \sqrt{\frac{1}{\lambda^2}-f_x^2 - f_y^2} \right] \, . 
\end{equation}
$$

It is clear that the Fresnel approximation in the frequency domain amounts to 

$$
\begin{equation}
	\frac{1}{\lambda}\sqrt{1 - (\lambda f_x)^2 - (\lambda f_y)^2} \approx 1 - \frac{(\lambda f_x)^2}{2} -  \frac{(\lambda f_y)^2}{2} \, ,
\end{equation}
$$
i.e., applying $\sqrt{1+\varepsilon} \approx 1+\frac{1}{2}\varepsilon$, but this time on the transfer function. Hence, the Fresnel approximation in the transfer function considers only low spatial frequencies, i.e., small angles with respect to the optical axis. 

(sec:fraunhofer)=
## Fraunhofer approximation
The second form of the Fresnel diffraction integral shows the integration of a multiplication of two functions in object coordinates. The presence of the exponential function in object coordinates makes the calculation of this integral cumbersome. Would it be possible to assume $\text{e}^{i\frac{k}{2z}(x_o^2+x_o^2)}\approx 1$ and under what circumstances? 

The exponential function on the object coordinates is approximately unity when 

$$
	z \gg \frac{k (\xi^2 + \eta^2)_{\text{max}}}{2} \, ,
$$

which is what we call the far field or Fraunhofer approximation. A more physical interpretation is that the phase from every object point is only dependent on the position in the object plane and the angle between the detection point and the center of the object plane, i.e., for a single detection point the lines from all object points run parallel. This of course only true when the detection point is far away. 

In the Fraunhofer approximation we are dealing with [Fraunhofer diffraction](https://en.wikipedia.org/wiki/Fraunhofer_diffraction) and the integral becomes

$$
	U(x_i, y_i, z)=\frac{\text{e}^{ikz}\text{e}^{i\frac{k}{2z}(x_i^2+y_i^2)}}{i \lambda z} \int_{\Sigma} U(x_o, y_o) \exp \left\{-i \frac{2 \pi }{\lambda z} \left[ x_i x_o + y_i x_o \right] \right\} \text{d}x_o \text{d}y_o \, .
$$(fraunhofer)

Equation {eq}`fraunhofer` shows that besides some constant pre-factors the field is a Fourier transform of the object field when we define 

$$
\begin{eqnarray}
	f_x &=& \frac{x_i}{\lambda z} \\
	f_y &=& \frac{y_i}{\lambda z} \, .
\end{eqnarray}
$$

The difference between Fresnel and Fraunhofer diffraction is shown in {numref}`fresnelfraun`. In Fresnel diffraction, a sum is made over the phase contribution of all points. The phase difference is generated by the path length differences given by the parabolic form. The lines connecting the object and detection points have different angles for both varying object and detection points. 

Fraunhofer diffraction is an integration of the phase contribution of all points. The phase difference is generated by the path length differences $x_o \sin \theta$ that lead to phases of $2\pi x_o \sin \theta/\lambda$. In the small angle approximation $\sin \theta \approx \theta$ we find that the phase for every point is approximately $2\pi x_o x_i/\lambda z$. This is exactly what is integrated over and amounts to a Fourier transform.

```{figure} fresnelfraun.png
---
height: 400px
name: fresnelfraun
---
Comparison between Fresnel and Fraunhofer diffraction.
```