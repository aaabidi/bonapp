class CreateReviews < ActiveRecord::Migration[5.2]
  def change
    create_table :reviews do |t|
      t.string :reviewer
      t.integer :rating
      t.string :review
      t.references :food, foreign_key: true

      t.timestamps
    end
  end
end
