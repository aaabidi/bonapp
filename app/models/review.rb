class Review < ApplicationRecord
  belongs_to :food

  validates :reviewer, presence: true
  validates :review, presence: true
  validates :rating, presence: true
  
end
