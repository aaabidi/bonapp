class User < ApplicationRecord
  validates :password, presence: true
  validates :name, presence: true
  validates :email, presence: true
end
