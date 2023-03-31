# serial-monitor

> Monitors a serial port and logs output to a log file

## Dependencies

- python
- pyenv
- poetry

## Usage

```shell
## Install dependencies
poetry install

## Run main script
poetry run ./src/main.py

## Lint with black
poetry run black .

## Test with pytest
poetry run pytest

## Update dependencies
poetry update
```

## Set up systemd

```shell
## Create a new systemd service for the serial monitor
sudo pico /lib/systemd/system/serial-monitor.service
## Paste in the contents of the example file, editing {USERNAME} or file locations as necessary
## Save and quit pico

## Reload systemd
sudo systemctl daemon-reload

## Enable the serial monitor service
sudo systemctl enable serial-monitor.service

## Reboot and confirm the service starts and runs as expected
sudo reboot
```

### Troubleshoot `systemd`

```shell
## Output logs from the serial monitor service
sudo journalctl -u serial-monitor.service

## Output the last few lines of the logs
sudo journalctl -u serial-monitor.service -n 5
```

## License

The MIT License (MIT)

Copyright (c) 2023 Dane Petersen
