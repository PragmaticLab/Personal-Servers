class CreateGoalsheets < ActiveRecord::Migration
  def change
    create_table :goalsheets do |t|
      t.date :time
      t.text :goals

      t.timestamps null: false
    end
  end
end
