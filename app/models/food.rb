class Food < ApplicationRecord
  has_many :reviews

  validates :name, presence: true
  validates :hall_name, presence: true
  validates :description, presence: true
end
