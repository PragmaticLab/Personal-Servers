class AddGoalsheetToTasks < ActiveRecord::Migration
  def change
    add_reference :tasks, :goalsheet, index: true
    add_foreign_key :tasks, :goalsheets
  end
end
