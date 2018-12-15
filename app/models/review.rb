class Review < ApplicationRecord
  belongs_to :food

  validates :reviewer, presence: true
  validates :review, presence: true
  validates :rating, presence: true, inclusion: { in: 1..5 }

end
