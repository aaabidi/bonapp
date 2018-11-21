class CreateFoods < ActiveRecord::Migration[5.2]
  def change
    create_table :foods do |t|
      t.string :name
      t.text :description
      t.references :user, foreign_key: true
      t.references :hall, foreign_key: true

      t.timestamps
    end
  end
end
