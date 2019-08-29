---
layout: post
title: "A Rant About Machine Learning + Some Clarification"
categories: programming education
---

Sitting on my couch, my roommate approaches me with an interesting question: can you use machine learning to do my homework?

I chuckled as I slowly stood up. "YES!", I proclaimed. I immediately flung my arms open, and like the black magic that machine learning is, used my algorithmic powers to generate some obscure function that would complete my friends homework. I shifted my right arm in front of me and snapped my fingers repeatedly, muttering the words machine learning and neural networks over and over.

My chanting became quicker as I spewed out spells such as K-Means, Gaussian Mixture Models, Random Forest, and Support Vector Machines. The room was filled with the sound of matrices and vector values, and big data began swirling around me as I searched for the homework answers. My friend watched in horror as I became engulfed in my algorithms and data, until suddenly everything stopped.

"I found it," I muttered.

My friend, too shocked to speak, could only watch as the Convolutional Neural Network appeared. I gently picked up my friends homework and fed it to the neurons. The sheet of paper effortlessly glided through the layers of alien-like cells, expanding and contracting along the way and sometimes even disappearing into the 13th dimension. Indeed, it was a sight to behold. At the end of the chain of layers, was a single sheet of paper. The answer key.

## Sorry that's not how machine learning works
But you already knew that! Right?! As absurd as the above story sounds (and yes I had fun writing it), the moral of the story still stands - machine learning is not well understood.

Before I continue, if you are someone involved in tech or have prior machine learning experience, kudos to you. It's a hard topic to understand and while I do have my fair share of experience, I've met many people who blew me away with their knowledge.

Here are a few examples of articles that throw around the words machine learning or neural network:

- [CNN: How elite investors use artificial intelligence and machine learning to gain an edge](https://www.cnn.com/2019/02/17/investing/artificial-intelligence-investors-machine-learning/index.html)
- [Wired: Artificial Intelligence Is Coming for Our Faces](https://www.wired.com/story/artificial-intelligence-fake-fakes/)
- [Forbes: The Amazing Ways YouTube Uses Artificial Intelligence And Machine Learning](https://www.forbes.com/sites/bernardmarr/2019/08/23/the-amazing-ways-youtube-uses-artificial-intelligence-and-machine-learning/#ba16fba58522)

I encourage to skim the article and pay close attention to the buzzwords being thrown around. Are you understanding anything about machine learning? Are they giving you any details at all about how machine learning was applied? Besides the fact that the article titles are all ~~absolute trash~~ clickbait, it's clear that the authors didn't bother looking into what "machine learning" actually meant. No algorithms, no simplistic description of how it was done, just buzzwords.

## How machine learning came about
To start, traditional machine learning techniques __are not new__. In fact, a lot of these techniques were developed from 1950 - 1970. Yes, techniques are continously being developed, but a lot of core concepts have remained the same. [Bayesian methods](https://en.wikipedia.org/wiki/Bayesian_inference), [Neural Networks](https://en.wikipedia.org/wiki/Artificial_neural_network), and other techniques were already being developed.

The big difference today is increased processing power computers provide us. Back in the day, using these algorithms was impractical due to the amount of data and difficult calculations required to achieve a decent result. As computers became more and more powerful, these techniques became more viable, leading to today, where GPUs and super computers are capable of processing petabytes of data for the purposes of training models.

If you're curious about the history, check out a [Timeline of Machine Learning](https://en.wikipedia.org/wiki/Timeline_of_machine_learning). It really puts into perspective how much time and work has been spent on this topic.

## But what IS machine learning then?
Good question. It'd be pretty crappy of me to write this whole rant, only to leave you hanging about the basics of machine learning. So let's start.

The purpose of machine learning is to discover a particular *function*. You assume that there is some input given (e.g. numerical data, images) that will achieve some desired output. Using data, you are attempting to find some sort of relationship between the input and desired output. But the question then becomes, how do you determine if a relationship exists?

One of the most important steps in machine learning is extracting *features*. How and what features you extract is completely up to the researcher, but this determines what sort of data your algorithm will be learning from. Like with most things, garbage in means garbage out. This applies to machine learning models as well.

After extracting features, you now have to determine what algorithm to use. This is just as tricky since different models will use different assumptions and work better in certain scenarios. What it boils down to is using the right tool for the right job. Using a linear regression classifier on nonlinear data will obviously give bad results, so use some other algorithm!

Machine learning has 3 main branches: supervised, unsupervised, and reinforcement.

The main difference between supervised and unsupervised machine learning, is that the former uses data that is labeled. For example, if your data is images, you might label them as cats or dogs (or whatever else you want). Unsupervised machine learning is simply ingests a bunch of data and tries to find previously unknown relationships. Finally, reinforcement machine learning learns very similar to humans. The machine will try different moves, get rewarded and punished based on their moves, and learn from their mistakes so that they select a better move next time.

Where the algorithms differ is how the data is processed and what assumptions are made. For example, if you use a Naive Bayes classifier (a supervised machine learning algorithm), it assumes that all features are independent (e.g. height and age). This is obviously not true in many scenarios, but this is what machine learning really boils down to: making tradeoffs. Do you want something that can generalize better? Or do you want it to work for a specific use case? How many different categories do you want to classify? How much data do you have? Are you able to extract relevant features from the data? Will you assume the data follows a particular statistical model?

It's quite logical honestly, but I feel that many of us get so caught up in the details that we just don't end up understanding anything at all about the topic. If you are interested more in the topic, I encourage you to use the power of the internet (*cough* Google *cough*) and learn about the details yourself. It's really neat when you understand how the algorithms work, and it gives you a much better sense of what goes on behind the scenes of machine learning.

On a final note, I've listed a few links that may be helpful below. Hope it helps, and hopefully this post helps clear up some of the black magic surrounding machine learning.


General Descriptions:
I suggest you just read the first few paragraphs then skip down to the list of popular algorithms. No need to get caught up in the jargon (unless you want to).
- [Wikipedia: Supervised ML](https://en.wikipedia.org/wiki/Supervised_learning)
- [Wikipedia: Unsupervised ML](https://en.wikipedia.org/wiki/Unsupervised_learning)
- [Wikipedia: Reinforcement ML](https://en.wikipedia.org/wiki/Reinforcement_learning)


Helpful Libraries:
These are different libraries I have used for my own machine learning projects. Numpy is pretty much the only requirement, but the other items here are pretty necessary as well depending on what you're doing. If you're new to all of this, stick with just numpy for now.
- [Numpy](https://numpy.org/): Required for machine learning
- [Scipy](https://www.scipy.org/): Has a lot of extra functionality and algorithms already built in
- [TensorFlow](https://www.tensorflow.org/): Deep learning library developed by Google. Very popular.
- [Keras](https://keras.io/): Similar to TensorFlow.
- [KerasRL](https://github.com/keras-rl/keras-rl): Library dedicated to supplying reinforcement learning algorithms compatable with OpenAI Gym
- [OpenAI Gym](https://gym.openai.com/): Framework that allows you to experiment with reinforcement learning algorithms in a game environment


Other Maybe Helpful Links:
- [Machine Learning Mastery](https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/): This blog has a lot of good machine learning posts as well as tutorials. It's helped me out a bunch when I get stuck.
- [Caltech Machine Learning Theory Course](https://work.caltech.edu/telecourse.html): Fantastic professor who breaks down difficult concepts into understandable components
- [Python Tutorial](https://docs.python.org/3/tutorial/): Python is the language of choice for machine learning. Learn it and run with it!
- [KNN Tutorial](https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_knn_algorithm_finding_nearest_neighbors.htm): There are plenty of tutorials available online. What's important is understanding the tradeoffs and theory. Otherwise, pick any tutorial you want!