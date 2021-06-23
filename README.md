
<h2 align="center">Offline Text To Speech (TTS) converter for Python3 </h2>




`pyttsx3` is a text-to-speech conversion library in Python. Unlike alternative libraries, **it works offline**.


## Installation :


	pip install pyttsx3

> If you get installation errors , make sure you first upgrade your wheel version using :  
`pip install --upgrade wheel`

### Linux installation requirements : 

+ If you are on a linux system and if the voice output is not working , then  : 

	Install espeak , ffmpeg and libespeak1 as shown below: 

	```
	sudo apt update && sudo apt install espeak ffmpeg libespeak1
	```


## Features : 

- ✨Fully **OFFLINE** text to speech conversion
- 🎈 Choose among different voices installed in your system
- 🎛 Control speed/rate of speech
- 🎚 Tweak Volume
- 📀 Save the speech audio as a file
- ❤️ Simple, powerful, & intuitive API


## Usage :

```python3
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```

**Single line usage with speak function with default options**

```python3
import pyttsx3
pyttsx3.speak("I will speak this text")
```

	
**Changing Voice , Rate and Volume :**

```python3
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()


"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

```




### **Full documentation of the Library**

https://pyttsx3.readthedocs.io/en/latest/


#### Included TTS engines:

* sapi5
* nsss
* espeak

Feel free to wrap another text-to-speech engine for use with ``pyttsx3``.

### Project Links :

* PyPI (https://pypi.python.org)
* GitHub (https://github.com/nateshmbhat/pyttsx3)
* Full Documentation (https://pyttsx3.readthedocs.org)


# gTTS

**gTTS** (*Google Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Write spoken `mp3` data to a file, a file-like object (bytestring) for further audio manipulation, or `stdout`. Or simply pre-generate Google Translate TTS request URLs to feed to an external program.
<http://gtts.readthedocs.org/>


## Features

-   Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
-   Customizable text pre-processors which can, for example, provide pronunciation corrections;

### Installation

    $ pip install gTTS

### Quickstart

Command Line:

    $ gtts-cli 'hello' --output hello.mp3

Module:

    >>> from gtts import gTTS
    >>> tts = gTTS('hello')
    >>> tts.save('hello.mp3')

See <http://gtts.readthedocs.org/> for documentation and examples.

### Disclaimer

This project is *not* affiliated with Google or Google Cloud. Breaking upstream changes *can* occur without notice. This project is leveraging the undocumented [Google Translate](https://translate.google.com) speech functionality and is *different* from [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

### Project

-   [Questions & community](https://github.com/pndurette/gTTS/discussions)
-   [Changelog](CHANGELOG.rst)
-   [Contributing](CONTRIBUTING.rst)

### Licence

[The MIT License (MIT)](LICENSE) Copyright © 2014-2021 Pierre Nicolas Durette & [Contributors](https://github.com/pndurette/gTTS/graphs/contributors)

