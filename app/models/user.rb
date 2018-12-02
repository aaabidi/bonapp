class User < ApplicationRecord
  has_many :comments
  validates :password, presence: true
  validates :name, presence: true
  validates :email, presence: true
end
