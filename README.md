# Pinger bot

This code allows you to ping multiple VDRs and give a sound notification when one of them pings. It'll continue to run till you kill the code "ctrl+c"

## Installation

Install python3 from https://www.python.org/

Install the requirements for the script.

```bash
pip install -r requirements.txt
```

## Usage

List all the IP address the ip.txt file with a line break. New ones can be added even after you start running the code. The code will go through each IP and ping for 3 sec to see if the system is online.

```bash
python3 pinger.py
```

## Contributing

[@rpai]('https://github.com/rpai9')

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License

Copyright (c) 2022 Rohith Pai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

The notification sound is from https://github.com/akx/Notifications repository.
Dual license -- choose between these two.

    * [CC Attribution 3.0 Unported](http://creativecommons.org/licenses/by/3.0/)
    * [CC0 Public Domain](http://creativecommons.org/publicdomain/mark/1.0/)

# Styling

Please use the [pep8](https://www.python.org/dev/peps/pep-0008/) style guide
