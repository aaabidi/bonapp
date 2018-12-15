class Amenity < ApplicationRecord
  has_many :statuses

  validates :name, presence: true
  validates :hall_name, presence: true
end
