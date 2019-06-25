#!/usr/bin/env ruby

require 'csv'

file_path = ARGV[0]
unless file_path
  puts "Please provide file path"
  exit(1)
end

file_out = ARGV[1]
unless file_path
  puts "Please provide output file path"
  exit(1)
end

if file_path == file_out
  puts "File in and file out can't be the same"
  exit(1)
end

$data = []
max_number = 4034

fh = open file_path
contents = fh.read
fh.close

previous_number = 0
contents.each_line { |line|
  next if line.strip.empty?
  # extract number, word and the rest
  /(?<number>\d+)\s+(?<word>[[:graph:][:word:]]+)\s?(?<part>\w+)?(?<other>.*$)?/ui =~ line
  if number && word
    number = number.to_i
    if !$data.fetch(number, nil) && number <= max_number
      $data[number] = {
        number: number,
        word: word,
        part: part,
        # transcription: '',
        other: other,
        # picture_url: '',
      }
      previous_number = number
    end
  end
  if !$data.empty? && $data.fetch(previous_number) && number != previous_number
    $data[previous_number][:other] += "#{line}\n"
  end
}

$data.reject! { |c| c.nil? || c.empty? }

# extract definitions and examples
$data.each_with_index{ |v, i|
  /(?<defn>.+?)•(?<example>.*$)/mu =~ v.fetch(:other, '')
  v[:definition] = if defn
     defn.strip.gsub("\n", '"\n"')
  else
    v[:other].strip.gsub("\n", '"\n"')
  end
  v[:examples] = example.strip.gsub(/\d+,?$/, '').strip.gsub("\n", '"\n"') if example
  v.delete(:other)
}


def show_missing()
  $data.each_with_index { |v, k|
    puts k unless v
  }
end

def show_missing_translation()
  $data.each { |v|
    puts v unless v[:definition]
  }
end

def show_data()
  puts $data
end

def write_csv()
  CSV.open(ARGV[1], "wb") do |csv|
    csv << %w(number word part transcription definition examples picture)
    $data.each { |v|
      csv << [v[:number], v[:word], v[:part], '', v[:definition], v[:examples], '']
    }
  end
end

show_missing
# show_data
show_missing_translation
write_csv
