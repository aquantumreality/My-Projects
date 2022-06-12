# Show, Attend and Tell: Neural Image Caption Generation with Visual Attention

## Contents
- [assets](https://github.com/aquantumreality/Model-Zoo/tree/main/NLP/Visual_Attention_Image_Captioning/assets)
- [scripts](https://github.com/aquantumreality/Model-Zoo/tree/main/CV-NLP/scripts)

## Summary
Image caption generation is the problem of generating a descriptive sentence of an image. The fact that humans (e.g you) can do this with remarkable ease makes this a very interesting/challenging problem for AI, combining aspects of computer vision (in particular scene understanding) and natural language processing.

In this work, an "attention" based framework is introduced into the problem of image caption generation. Much in the same way human vision fixates when you perceive the visual world, the model learns to "attend" to selective regions while generating a description. Furthermore, in this work we explore and compare two variants of this model: a deterministic version trainable using standard backpropagation techniques and a stochastic variant trainable by maximizing a variational lower bound. 

## How does it work? : 
The model brings together convolutional neural networks, recurrent neural networks and work in modeling attention mechanisms. 


![From a high level, the model uses a convolutional neural network as a feature extractor, then uses a recurrent neural network with attention to generate the sentence](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/model_diag.png 'Model Working')
**Approach Overview**: In step (2), image features are captured at lower convolutional layers. In step (3), a feature is sampled, fed to LSTM to generate corresponding word. Step 3 is repeated K times to generate K-words caption 

If you are not familiar with these things, you can think of the convolutional network as an function encoding the image ('encoding' = f(image)), the attention mechanism as grabbing a portion of the image ('context' = g(encoding)), and the recurrent network a word generator that receives a context at every point in time ('word' = l(context)).

This model learns where to look.

As you generate a caption, word by word, you can see the model's gaze shifting across the image.

This is possible because of its Attention mechanism, which allows it to focus on the part of the image most relevant to the word it is going to utter next.

Here are some captions generated on test images not seen during training or validation:

![1](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/babycake.png)
-----------------------------------------------------------------------------------------
![2](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/boats.png)
-----------------------------------------------------------------------------------------
![3](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/dogtie.png)

## The Model in Action
![t1](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/4028.gif) ![t2](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/7288.gif) ![t3](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/7600.gif) ![t4](https://github.com/aquantumreality/Model-Zoo/blob/main/NLP/Visual_Attention_Image_Captioning/assets/13936.gif)
