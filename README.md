# Pomodoro Timer :alarm_clock:

Simple timer app to **take a break every 20 minutes for 20 seconds**


## Usage

1. Download installer from [Pomodoro Timer Installer](#)
2. Install it on system and start the app
3. Get to work :computer: , Pomodoro Timer will take care fo the rest :sunglasses:

**Note:** To stop the timer open task manager and in process tab find **pythonw.exe** & kill it.


## Development


### Prerequisites

- Your favurite editor viz. PyCharm, Vim, Sublime Text, etc.
- Python 2.7 Release


### Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Python 2.7.9](https://www.python.org/downloads/release/python-279/) - Python 2.7 Release
* [pynsist 1.12](https://pynsist.readthedocs.io/en/latest/) - Tool to build Windows installers
* [NSIS 3.02.1](http://nsis.sourceforge.net/Download) - Professional open source system to create Windows installers

### Build Instructions

1. Download or clone the repository
2. Install **[NSIS 3.02.1](http://nsis.sourceforge.net/Download)** as required for **pynsist**
3. Install build dependencies ``pip install -r requirements.txt``
4. Build using ``pynsist installer.cfg``
5. Get the **Pomodoro_Timer_1.0.exe** under ``build/nsis``


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for contributions.


## License
-------
    Copyright 2017 Pomodoro Timer Developers

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
---
