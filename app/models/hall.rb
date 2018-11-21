class Hall < ApplicationRecord
  has_many :foods
  has_many :amenities
  validates :name, presence: true
end
