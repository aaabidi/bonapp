require 'json'
json = File.read('leutnerBreakfast.json')
menu = JSON.parse(json)
puts(menu)

menu.each do |name|
    item = Food.create :name => name, :hall_name => "Leutner"
end
