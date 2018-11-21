class Food < ApplicationRecord
  belongs_to :user
  belongs_to :hall
  has_many :comments
end
