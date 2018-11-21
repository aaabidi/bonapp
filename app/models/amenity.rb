class Amenity < ApplicationRecord
  belongs_to :user
  belongs_to :hall
  has_many :statuses
  validates :status, presence: true
  validates :name, presence: true
end
