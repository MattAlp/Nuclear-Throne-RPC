# Nuclear Throne RPC


About this project
======
This Python script serves as an interface between the [Nuclear Throne Stream Key API](https://nuclearthrone.com/streamkey/) and the [Discord Rich Presence API](https://discordapp.com/rich-presence).

How to use this
======
Prior to running this, you'll need the appropriate packages: simply run

    pip install -r requirements.txt

Afterwards, you'll need three things:

1. **Your Nuclear Throne Stream Key**
	* To find this, go to Menu/Settings/Game/Stream Key
	* Once a key is generated, it can be used for an indefinite period 		of time, but will need to be re-enabled upon game launch each time
2. **Your Steam64ID**
	* This can be obtained through a web service such as [this one](https://steamid.io/)
3. **A Discord Application ID**
	* Unless you wish to use your own ID and custom resources, this should remain unmodified
	
These values must then be configured within ```config.py```; to start the program, simply run ```main.py```.

Upcoming Features
======
In no particular order:
* Large tiles with B-Skin support (once I get around to resizing the game files and manually upload them to Discord)
* Small tiles to represent the current crown
* Comments and PEP8 consistency

Thanks to
======
Vlambeer, the Nuclear Throne Wiki, [/r/nuclearthrone](https://reddit.com/r/nuclearthrone), and [Sankarsan Kampa](https://github.com/k3rn31p4nic) for their wonderful [discoIPC](https://github.com/k3rn31p4nic/discoIPC) module.

Final Notes
======
This is my first project on Github, contributions and stars are greatly appreciated.

Have a question? DM me at [/u/NotMattA](https://reddit.com/u/NotMattA) on reddit!