# Jibot

### About

A conversational assistant to order pizza


i have  :

* added new data
* updated domain file
* removed useless actions and adding new ones
* added new rules and stories
* added the feedback feature
* tested and evaluated on 2 different pipelines
* connected the bot with Alexa skill

This chatbot was built using [Rasa](https://rasa.com/docs/getting-started/). Tutorials on how to develop a similar chatbot are avaible the offical website and also on [Youtube](https://www.youtube.com/watch?v=rlAQWbhwqLA&list=PL75e0qA87dlHQny7z43NduZHPo6qd-cRc).

you can find a demo of Jibot in this [link.](https://drive.google.com/drive/folders/1_fACdk-jXpLgPhgtMaODoHcMvSXY5N5Z?usp=share_link)

### Getting Started

> install first [Rasa](https://rasa.com/docs/rasa/user-guide/installation/#installation)

### Train the chatbot

```
rasa train
```

### Test chatbot

```
rasa test
```

### Talk to chatbot

```
rasa shell
```

In case it doesn't predict any response please use specifying the model folder:

```commandline
rasa shell -m models/
```
