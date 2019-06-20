# Fishy

Tk GUI app for learning words corpus.

Name comes from, you guess it, [this little fishy](https://en.wikipedia.org/wiki/List_of_races_and_species_in_The_Hitchhiker%27s_Guide_to_the_Galaxy#Babel_fish).


## Corpus CSV File format

- Number
- Word
- Part of the speech
- Transcription
- Translation/Meaning/Definition
- Examples (separated by |)
- Picture URL


## Usage

* Clone repository
* `cd Fishy`
* Run `make install`
* Create CSV file with words in the aforementioned format and put it somewhere
* Modify path to file in config `$HOME/.fishy_app.cnf`
* Run `fishy` (Or `fishy &` to free console)


## Development

To launch unit tests run `make test`.
