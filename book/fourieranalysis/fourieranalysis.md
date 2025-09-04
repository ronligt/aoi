# Fourier analysis

As we have seen from the Angular Spectrum description, the optical wavefield can be described as a decomposition in plane wave functions. Since, for propagating waves, the $z$-component of the plane wave can be calculated for any $x,y$ plane wave component, the entire plane wave can be determined from the 2D Fourier transform, denoted with $\cal F$, of the input field. In math notation the Fourier transform is applied on a function of the lateral coordinates indicate with lowercase, e.g., $g(x,y)$. The Fourier transform of $g(x,y)$ is indicated with uppercase $G(f_x, f_y)$ or as $\mathcal{F}\{g(x,y)\}$. Here we will discuss the most important 2D Fourier transform properties in the context of optical imaging.

## The Fourier transform
The two dimensional Fourier transform is defined as and integral over spatial coordinates with the minus sign in the exponent

$$
	{\cal F}\{g(x,y)\}=G(f_x, f_y) = \iint_{-\infty}^{\infty} g(x, y) \text{exp}[-i 2 \pi (x f_x + y f_y)] \text{d} x \text{d} y \, .
$$(Fouriertrafo)

In Fourier optics, the input function usually is an input field. The output is the field as a funtion of spatial frequencies. Similarly the inverse Fourier transform is defined as an integral over spatial frequencies with the plus sign in the exponent

$$
	g(x,y)={\cal F}^{-1}\{G(f_x,f_y)\} = \iint_{-\infty}^{\infty} G(f_x, f_y) \text{exp}[+i 2 \pi (x f_x + y f_y)] \text{d} f_x \text{d} f_y \,.
$$(inverseFouriertrafo)

## Fourier transform properties in optical imaging

### Linearity
The Fourier transform is linear, which means that the Fourier transform of a sum of amplitude scaled inputs is the sum of the amplitude scaled Fourier transform of the inputs. In mathematical form

$$
	{\cal F} \{ \alpha g(x,y)  + \beta h(x,y)\} = \alpha {\cal F} \{ g(x,y) \} + \beta {\cal F} \{ h(x,y) \} \, .
$$ 

The wave equation is a linear equation so Fourier analysis can be applied to decompose optical wavefields in, e.g., plane waves, and analyse their propagation. In optical imaging the image formation is linear in field for coherent imaging, however, as you will see it is linear in intensity for incoherent imaging.

### Stretch 
A scaling in the coordinates leads to an inverse scaling of the frequencies. This can be understood by realizing that to represent sharp spatial features you need a large spread of spatial frequencies. In mathematical form this is written as
 
$$
	{\cal F} \{  g(\alpha x, \beta y) \} = \frac{1}{|\alpha \beta|} G\left( \frac{f_x}{\alpha}, \frac{f_y}{\beta} \right) \, .
$$ 

This property manifests itself in Fraunhofer diffraction where a narrower slit gives rise to a broader diffraction pattern. In optical imaging, magnification scales the object coordinates to image coordinates. This stretching causes a concomitant scaling of the spatial frequencies. A spatial expansion causes a frequency shrinkage and vice versa.

### Shift theorems
A shift in spatial frequency results in a multiplication of the spatial function with an exponential linear phase.

$$
	{\cal F}^{-1} \{  G(f_x - \alpha, f_y- \beta) \} = \text{exp}[i 2 \pi (x \alpha + y \beta)]  g\left( x, y \right) \, .
$$ 

An example is that of a a tilted wavefront, which is represented by a multiplication with a linear phase exponent. This results in a shift in the angular spectrum. Also a aperture illuminated with a tilted plane wave gives rise to a shift of the diffraction pattern.

A shift in space results in a multiplication of the frequency response with a linear phase exponent. In mathematical form

$$
	{\cal F} \{  g(x - \alpha, y- \beta) \} = \text{exp}[-i 2 \pi (\alpha f_x + \beta f_y)]  G\left( f_x, f_y\right) \, .
$$ 

An example is a shift of the object, which corresponds to a linear phase in the Fourier plane.

### Convolution
The convolution, or folding operation, is the cornerstone on linear system analysis. It states that the output can be generated as the sum of folded responses to a $\delta$-function input. For 2D systems the response to a $\delta$-function input is called the point spread function (PSF). Using the Fourier transform operation it can be shown that the Fourier transform of a convolution is the product of the transfer functions. 

$$
	{\cal{F}}\left\{ \int_{-\infty}^{\infty} g(\xi, \eta)h(x-\xi, y-\eta) \text{d}\xi \text{d}\eta \right\} = G(f_x, f_y)H(f_x, f_y)\, .
$$   

The Angular Spectrum, Fresnel diffraction, and optical imaging processes all can be described as a convolution with a PSF. Hence, in the Fourier domain these operations are described by a multiplication with a transfer function.

### Autocorrelation
The autocorrelation is closely related to the convolution albeit that it doesn't involve a folding operation. It merely shifts the function with itself and calculates the overlap between them. In mathematical form

$$
	{\cal{F}}\left\{ \int_{-\infty}^{\infty} g(\xi, \eta)g^*(\xi - x, \eta -y) \text{d}\xi \text{d}\eta \right\} = G(f_x, f_y)G^*(f_x, f_y)=|G(f_x, f_y)|^2
$$

The autocorrelation is of importance for incoherent imaging where the optical transfer function is determined by the autocorrelation of the pupil function. When the functions are real-valued and symmetric the autocorrelation and convolution are identical.

### Parseval's theorem
This theorem essentially states that energy is conserved in both the spatial and frequency domain. Mathematically, this is described as

$$
	\int |g(x,y)| \text{d}x\text{d}y = \int |G(f_x, f_y)|^2 \text{d}f_x\text{d}f_y \, .
$$ 

Considering the fact that the Fraunhofer diffraction pattern is the Fourier transform of the aperture the energy within the aperture (expressed as a function of spatial coordinates) is equal to the energy in the diffraction pattern (expressed as a function of frequency coordinates).

### Fourier identity
The Fourier transform of the Fourier transform of a function is a mirror copy of the function. In mathematical form

$$
	{\cal{F}}\{ \, {\cal{F}}\{g(x,y)\} \, \} = g(-x, -y) \, .
$$

This property plays a key role in the description of 4$f$-imaging systems. When aligned in a telecentric way, the optical system performs a Fourier transform of a Fourier transform resulting in an inverted image.

## Fourier transform pairs in optical imaging
Besides the aforementioned Fourier transform properties we calculate the Fourier transforms using basic Fourier transform pairs.

### Fourier transform pairs for Cartesian separable functions
Whenever the 2D function that is to be Fourier transformed can be written as the product of a function in $x$ and a function in $y$ the Fourier transform is separable. In that case the problem can be split up as a multiplication of two 1D Fourier transforms, more formally for a function $g(x,y)=f(x)h(y)$

$$
	{\cal{F}}_{xy}\{  g(x,y) \} = {\cal{F}}_{xy}\{ f(x) h(y) \} = {\cal{F}}_{x}\{ f(x) \} {\cal{F}}_{y}\{ h(y) \}\, 
$$

where ${\cal{F}}_{xy}$ denotes the two-dimensional Fourier transform according to Eq. {eq}`Fouriertrafo` where the subscript $xy$ denotes a two-dimensional Fourier transformation and $x$ or $y$ a one-dimensional Fourier transformation.

$$
\begin{equation}\begin{array}{|c c c|l}
	\exp[- \left(\left(\frac{x}{a}\right)^2 + \left( \frac{y}{b} \right)^2 \right)] & \leftrightarrow & |ab| \text{exp}\left[ - \pi \left(a^2f_x^2 + b^2 f_y^2 \right)\right] & \text{Gaussian function}\\
	\text{rect}\left(\frac{x}{a}\right)\text{rect}\left(\frac{y}{b} \right) & \leftrightarrow & |ab|\text{sinc}(a f_x)\text{sinc}(b f_y) & \text{Rectangular aperture width} \, a, b \\
	\delta(ax, by) & \leftrightarrow & \frac{1}{|ab|} & \text{Scaled delta function} \\
	\Lambda(ax)\Lambda(by) & \leftrightarrow & \frac{1}{|ab|}\text{sinc}^2\left(\frac{f_x}{a}\right)\text{sinc}^2\left(\frac{f_y}{b}\right) & \text{Triangle function} \\
	\text{exp}[i 2 \pi (ax + by)] & \leftrightarrow & \delta(f_x -a)\delta(f_y -b) & \text{Phase ramp} \\
	\text{comb}(ax)\text{comb}(by) & \leftrightarrow & \frac{1}{|ab|}\text{comb}\left(\frac{f_x}{a}\right)\text{comb}\left(\frac{f_y}{b}\right) & \text{Pulse comb} \\
\end{array}\end{equation}
$$(Fouriertransformpairs)

### Fourier transform pairs for seperable functions in polar coordinates
Consider a function in polar coordinates $g(r, \theta)$ of which we want to calculate the Fourier transform. In general, the Fourier transform is described in angle $\theta$ and radial frequency $f_r$, where the function $g$ is periodic with period $2\pi$ in $\theta$. For the class of functions that is separable in $r$ and $\theta$, i.e.,

$$
	g(r, \theta) = g_{\Theta}(\theta) g_R(r) \, ,
$$

the Fourier transform is given by a Fourier series in $\theta$ and a Hankel function in $f_r$. Here, the focus is on circularly symmetric functions, i.e. $g(\theta)$ is constant and $g(r, \theta)=g_R(r)$. In that case the Fourier transform is calculated as

$$
	G(f_r) = 2 \pi \int_0^{\infty} r g_R(r) J_0(2 \pi r f_r) \text{d}r \, ,
$$

where the integration is over $r$ to yield a Fourier transform as a function of radial spatial frequency $f_r$. The function $J_0(x)$ is the zero order Bessel function of the first kind. Also for the radial Fourier transform, basic Fourier transform properties hold, such as the identity relation

$$
	{\cal{B}}^{-1}\{{\cal{B}}\{g_R(r)\}\}=g_R(r) \,
$$

and the scaling relation

$$
	{\cal{B}} \{g_R(a r)\} = \frac{1}{a^2}G \left( \frac{f_r}{a} \right)  \, .
$$

A useful relation to calculate the radial Fourier transform is

$$
	\int_0^x \alpha J_0(\alpha) \text{d}\alpha = x J_1(x) \, ,
$$

with $J_1(x)$ the first order Bessel function of the first kind. 
