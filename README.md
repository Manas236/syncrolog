# SyncroLog

A lightweight CLI tool designed to monitor local project directories for specific file extension changes and automatically append a timestamped summary to a local daily markdown log file. This tool is perfect for developers or writers who want to maintain an automated activity journal of their progress without manually typing what they worked on. It uses the watchdog library to watch the filesystem and stores session logs in simple text files. Users can configure which directories to watch and which file types to track via a local config file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Future Work](#future-work)
- [License](#license)

## Installation

```bash
git clone <repo-url>
cd syncrolog
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Run the main entry point to start SyncroLog.

## Project Structure

```
├── cli.py
├── config.py
├── watcher.py
├── logger.py
├── utils.py
├── requirements.txt
└── README.md
```

## Modules

- **entry_point**: Core module for entry_point functionality.
- **configuration**: Core module for configuration functionality.
- **core**: Core module for core functionality.
- **utils**: Core module for utils functionality.

## Future Work

- [ ] Add comprehensive test suite
- [ ] Implement CI/CD pipeline
- [ ] Add Docker support
- [ ] Improve error handling and edge cases
- [ ] Add configuration documentation
- [ ] Performance optimization

## License

This project is licensed under the MIT License.
