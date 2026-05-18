# bd-labelmaker

Change the card fonts without restarts or code changes.

This will likely not receive any support nor maintenance, but I'll take PRs.

## Installation

Add the following lines to your `config/extra.toml` (create it if it doesn't exist):

```toml
[[ballsdex.packages]]
location = "git+https://github.com/dormieriancitizen/bd-fontchanger.git"
path = "bd_fontchanger"
enabled = true

```

## Usage

To use, first add a font (otf or ttf file) in the `Font configs` panel, then run `@botping fontchanger_reloadconf` (or use your prefix).

Subsequent renders will use those fonts.

For reference, the default sizes are:
TITLE: 170
ABILITY_NAME: 110
ABILITY_DESC: 75
STATS: 130
CREDITS: 40

## Example

<img width="862" height="948" alt="image" src="https://github.com/user-attachments/assets/ae65baf6-e0f2-4472-9cf9-d7bc435760a1" />

## Notes

This does not currently allow you to change font colors or outlines, since that's a more complicated process.
