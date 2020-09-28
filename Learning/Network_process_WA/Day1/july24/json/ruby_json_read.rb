require 'json'
JSON.load(File.open("data.json")).each { |k, v|
            puts "#{k} -> #{v}\n" 
}


