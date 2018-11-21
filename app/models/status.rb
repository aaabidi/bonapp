class Status < ApplicationRecord
  belongs_to :amenity
  belongs_to :user
  validates :status, presence: true
end
