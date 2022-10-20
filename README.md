# Simulator

Simulator is a Python program that enables you to simulate a soccer/football match between two of your favorite teams.

# Dependencies

Your device should be able to support running Python programs. To ensure the program runs successfully, you may also need to run the following commands:

```bash
pip3 install requests
pip3 install bs4
```

These are necessary packages to facilitate the scraper portion of the program.

If you would like to run the React interface, you should make sure to have node package manager installed on your device. Change your directory to the frontend, then run the following command: 

```bash
npm i
```

# Running The Program

To run the program on the command line, all you need to do is run the following commands:

```bash
cd backend
python3 simulator.py
```

Ensure that you choose teams that are supported by the simulator, otherwise the program will throw a KeyError.

To interact with the program on the React frontend, in addition to running the above command, you should also open a new terminal, then run the following commands:

```bash
cd frontend
npm start
```

# RoadMap

- Google Sheets support for inputting team information.
- Ability for users to create leagues and save them in local storage.
- More team support.

## License
[MIT](https://choosealicense.com/licenses/mit/)