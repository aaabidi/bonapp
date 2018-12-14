class CreateStatuses < ActiveRecord::Migration[5.2]
  def change
    create_table :statuses do |t|
      t.string :reviewer
      t.string :status
      t.references :amenity, foreign_key: true

      t.timestamps
    end
  end
end
