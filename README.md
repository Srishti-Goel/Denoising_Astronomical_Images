# Denoising_Astronomical_Images  
## Aim of the Project  
Noises plague astronomical noise and can be a huge set-back for the study of astronomy, especially because our signals are so faint and the SNR is already significantly low. Some common forms of noise include:
<list>
- **Instrument Noise** which occurs due to the thermal excitation of the electrons in the sensor leading to a so called "dark current".
- **Read-out Noise** which occurs due to the electronics of the CCD used to record the intensity
- **Photon-shot Noise** which occurs due to the variation of the number of photons from distant sources due to variations like refractive index of the atmosphere, or in the case of space-based telescopes like the Hubble Space Telescope (HST), the inter-galactic medium. This is mostly reduced by long-exposure images
</list>

This project aims to reduce noises in astronomical images using Machine Learning to learn patterns of the noise.  

## Convolutional Neural Networks(CNNs)  
Convolutional Neural Networks are used widely in the processing of images. These work by convolving the input images with a successively shifting filter to capture the relations between near-by pixels  

## Details  
To train the model, we artificially generate images with random noise with statistics similar to the ones actually expected in our images. This allows us to have a ground truth to which the CNN is trained toward. Thus, this is a supervised learning task.  
Images are taken from actual HST archives from the F555W and F606W filters. There was not much gain noticed by using the same image from both filters.   
We also compared the results of the models when the exposure time was inputted to the model, and when it was not inputted. Results show that the exposure-time-known model were significantly better at removing Photon-shot Noise.  
