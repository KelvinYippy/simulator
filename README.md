# Simulator

Simulator is a Python program that enables you to simulate a soccer/football match between two of your favorite teams.

# Dependencies

Your device should be able to support running Python programs. To ensure the program runs successfully, you may also need to run the following commands:

```bash
pip3 install requests
pip3 install bs4
```

These are necessary packages to facilitate the scraper portion of the program.

# Running The Program

To start the program, all you need to do is run the following commands:

```bash
cd backend
python3 simulator.py
```

Ensure that you choose teams that are supported by the simulator, otherwise the program will throw a KeyError.

# RoadMap

- Building out a React client for users to interact with as opposed to using command-line.
- Google Sheets support for inputting team information.
- Ability for users to create leagues and save them in local storage.

## License
[MIT](https://choosealicense.com/licenses/mit/)