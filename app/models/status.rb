class Status < ApplicationRecord
  belongs_to :amenity

  validates :reviewer, presence: true
  validates :status, presence: true
  
end
