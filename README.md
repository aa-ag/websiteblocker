# Website Blocker

Python script to block a list of websites during a pre-set schedule.

### Architecture

The script maps hostnames of websites to localhost address.

## To run

- `sudo crontab -e`
- `i` (insert)
- `@reboot script.py`
- `esc`
- `:wq`