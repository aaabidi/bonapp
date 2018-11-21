class Comment < ApplicationRecord
  belongs_to :food
  belongs_to :user
  validates :title, presence: exists
end
