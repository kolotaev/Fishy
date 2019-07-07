# Fishy

Tk GUI app for learning words corpus.

Name comes from, you guess it, [this little fishy](https://en.wikipedia.org/wiki/List_of_races_and_species_in_The_Hitchhiker%27s_Guide_to_the_Galaxy#Babel_fish).

**Currently tested only on MacOS.**


## Corpus CSV File format

- Number
- Word
- Part of the speech
- Transcription
- Translation/Meaning/Definition
- Examples (separated by |)
- Picture URL


## Usage

* Install [SoX](http://sox.sourceforge.net), with MP3 support.
* Clone repository
* `cd Fishy`
* Run `make install`
* Create CSV file with words in the aforementioned format and put it somewhere
* Modify path to file in config `$HOME/.fishy_app.cnf`
* Run `fishy` (Or `fishy &` to free console)


## Example configuration
```ini
[window]
initial-size = 800x600
resizable = yes
word-font-family = Courier
word-font-size = 22
explain-font-family = Courier
explain-font-size = 16

[popup]
show_timeout_value = 30
show_timeout_unit = min
start_time = 13.00
end_time = 22.00

[corpus]
file_path = /path/to/french-words-db.csv
language = de
additional-translate-to-lang = ru
speech-provider = google

[learn]
words-repeat = 30
repeat-intensity = 3
repeat-strategy = long-steps-back

[run]
current-pointer = 1
repeat-counter = 0
```


## Development

To launch unit tests run `make test`.
