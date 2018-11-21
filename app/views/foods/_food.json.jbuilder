json.extract! food, :id, :name, :description, :user_id, :hall_id, :created_at, :updated_at
json.url food_url(food, format: :json)
