require 'json'
json = File.read('fribleyLunch.json')
menu = JSON.parse(json)
puts(menu)

menu.each do |name|
    item = Food.create :name => name, :hall_name => "Fribley"
end
