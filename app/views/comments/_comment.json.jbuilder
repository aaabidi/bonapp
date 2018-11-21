json.extract! comment, :id, :rating, :body, :food_id, :user_id, :created_at, :updated_at
json.url comment_url(comment, format: :json)
