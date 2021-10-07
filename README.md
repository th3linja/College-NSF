# College-NSF
A project that takes a list of U.S. community colleges provided mostly from Wikipedia and searches for related NSF awards. All data is then exported and collected through script. Results are found here.

## Getting Started
The purpose of this project was a client specific request who wanted to efficiently collect a specific data, in this case: NSF awards of various U.S. community colleges from a specific site. The data is no secret and is publicly available for all to see, so the results are included in the repo as well. This script was working at the time of its execution (6/8/2020) and may change in the future since the web scraping is specified to certain tags/elements of the site scraped.

## Prerequisites
* Python
* shutil
* requests
* BeautifulSoup 4
* selenium

## Installing
Head over to [Python.org](https://www.python.org/) to download the latest version of Python if you haven't already. Make sure to enable pip in  `Optional Features` when installing. After installing, head over to Advanced System Settings -> Environment Variables and add Python into PATH. Open the command prompt (cmd) and run the command `pip3 install shutil`, `pip3 install requests`, `pip3 install bs4`, and `pip3 install selenium`.

## Running Tests
* Replace all file paths with your own local directory.
* The current state of the scrip is set to call the function once, sinmply replace that with a loop and evrything should work fine.

## Authors
th3linja
